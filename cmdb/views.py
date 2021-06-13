from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import HttpResponseRedirect
import pymysql

# 连接数据库配置信息
con = pymysql.connect(
    # 数据库主机名
    host="localhost",
    # 端口号
    port=3306,
    # 用户名
    user="root",
    # 密码
    passwd="root",
    # 数据库名
    db="njtc_django",
    # 编码格式
    charset="utf8"
)
# 得到游标
cursor = con.cursor()


# Create your views here.
def index(request):
    # 返回到一个htmml
    return render(request, "index2.html")


# 登录方法
def login(request):
    # 返回一个字符串给浏览器
    # return  HttpResponse("hello world!")
    # 返回到一个html
    return render(request, "login2.html")


# 登录验证
def checkLogin(request):
    # 获取用户输入的数据
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)
    # print(username,password)
    # 登录验证
    number = cursor.execute("select * from user where username='%s' and password='%s'" % (username, password))
    # 返回多少条记录
    if number > 0:
        # 登录成功
        # 进入主页面(展示所有记录，并可以增删改)
        # 重定向到主页面
        return HttpResponseRedirect("/showUsers/")

    else:
        # 登录失败
        return render(request, "login2.html", {"info": "账号或者密码错误！"})


# 展示主页面
def showUsers(request):
    # 查询出所有的数据
    cursor.execute("select * from user")
    # 使用列表保存查询到的数据
    user_list = []
    for x in cursor.fetchall():
        # 将每列数据存储到对应的字典value中
        user_dict = {"userId": x[0], "username": x[1], "password": x[2]}
        # 将每个字典子元素添加到列表中
        user_list.append(user_dict)
    #     返回数据到数据显示页面
    return render(request, "success2.html", {"data": user_list})


# 跳转到增加页面
def addUserUI(request):
    return render(request, "addUser.html")


# 新增用户
def addUser(request):
    # 获取用户输入的数据
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)
    # 执行sql insert语句插入数据
    cursor.execute("insert into user(username,password) values ('%s','%s')" % (username, password))
    # 提交事物
    con.commit()
    # 重定向到主页面
    return HttpResponseRedirect("/showUsers/")


# 根据用户id来删除用户
def delUser(request):
    # 获取用户输入的数据
    userId = request.GET.get("userId", None)
    # 将用户获取到的id转换为number类型
    id = int(userId)
    cursor.execute("delete from user where id = %d" % id)
    con.commit()
    # 重定向到主页面
    return HttpResponseRedirect("/showUsers/")


# 点击修改按钮,跳转到修改页面
def changeUser(request):
    # 获取到用户的id
    userId = request.GET.get("userId", None)
    id = int(userId)
    # 查询该id对应的用户信息
    cursor.execute("select * from user where id = %d" % id)
    # 定义一个用户字典,用于存储数据库查询到的数据
    user_dict = {}
    # for循环遍历查询到的该条记录
    for x in cursor.fetchall():
        # 将id,name,password等分别存储到字典的value中
        user_dict = {"userId": x[0], "username": x[1], "password": x[2]}
    # 返回数据到changeUser.html页面
    return render(request, "changeUser.html", {"data": user_dict})


# 点就修改页面的修改按钮,提交修改数据到数据库中
def AlterInfo(request):
    # 获取changeUser.html传过来的id
    user_id = request.GET.get("userId")
    userId = int(user_id)
    # 获取当前页面修改后的用户信息
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)
    # 通过sql update语句更新数据库中的数据
    cursor.execute("update user set username = '%s', password='%s' where id = %d " % (username, password, userId))
    # 提交事物
    con.commit()
    # 重定向到主页面
    return HttpResponseRedirect("/showUsers/")
