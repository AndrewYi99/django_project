"""mysiteRjsf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from cmdb import views

urlpatterns = [
    path('index/', views.index),  # 测试页面
    path('login/', views.login),  # 登录页面
    path('checkLogin/', views.checkLogin),  # 登录校验
    path('showUsers/', views.showUsers),  # 显示用户方法
    path('addUserUI/', views.addUserUI),  # 添加用户视图
    path('changeUser',views.changeUser), # 跳转到修改用户数据界面
    path('AlterInfo',views.AlterInfo), # 修改并提交用户数据
    path('addUser/', views.addUser),  # 添加用户方法
    path('delUser/', views.delUser),  # 删除用户方法

]
