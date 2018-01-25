# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, RequestContext
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt

from learn.forms import QueryForm
from learn.models import Employee
from django.db.models import Q

class User:
    def __init__(self, name, age, sex, where, job, hobby):
        self.name = name
        self.age = age
        self.sex = sex
        self.where = where
        self.job = job
        self.hobby = hobby

def add(request, a, b):
    a = int(a)
    b = int(b)
    print a, b
    c = a + b
    return HttpResponse(c)


def showUserInfo(request, userId):
    """
    基本的模板渲染操作
    :param request:
    :param userId:
    :return:
    """
    userId = int(userId)
    # 查询用户信息
    user = User('libaoshen', 23, 'male', 'hubei', 'programmer', 'sleep')

    # 创建模板
    t = Template("<html>{{user.name}}:{{user.age}}</html>")
    # 创建上下文
    c = Context({'user': user})
    # 数据渲染
    return HttpResponse(t.render(c))


def showUserInfo2(request, userId):
    """
    模板文件渲染操作
    :param request:
    :param userId:
    :return:
    """
    userId = int(userId)
    # 查询用户信息
    user = User("libaoshen", 23, 'male', 'hubei', 'programmer', 'sleep')

    # 创建模板
    t = get_template("userInfo.html")
    # 创建上下文
    c = Context({'user': user})
    # 数据渲染
    return HttpResponse(t.render(c))


def showUserInfo2(request, userId):
    """
    模板文件渲染操作
    :param request:
    :param userId:
    :return:
    """
    userId = int(userId)
    # 查询用户信息
    user = User("libaoshen", 23, 'male', 'hubei', 'programmer', 'sleep')

    # 数据模板创建、渲染一步到位
    return render_to_response("userInfo.html", Context({'user': user}))

def insertEmployee(request):
    """
    向数据库中插入数据
    :param request:
    :return:
    """
    employ1 = Employee(name="libaoshen", age=23, sex='m', where='hubei', job='programmer', hobby='sleep1')
    employ2 = Employee(name="wangzhi", age=22, sex='m', where='hubei', job='programmer', hobby='sleep2')
    employ3 = Employee(name="yanglin", age=21, sex='f', where='hubei', job='programmer', hobby='sleep3')

    employ1.save()
    employ2.save()
    employ3.save()

    return HttpResponse("保存成功")

def getAllEmployee(request):
    """
    获取所有用户信息
    :param request:
    :return:
    """
    userList = Employee.objects.all()

    return render_to_response("employeeInfo.html", Context({"userList": userList}))


def getOne(request, name):
    """
    通过姓名获取用户信息获取一条信息
    :param request:
    :param name:
    :return:
    """
    userList = Employee.objects.get(name=name)

    return render_to_response("userInfo.html", Context({"user": userList}))


def getEmployeeByName(request, name):
    """
    通过姓名获取用户信息
    :param request:
    :param name:
    :return:
    """
    # userList = Employee.objects.filter(name=name)
    userList = Employee.objects.filter(name__contains=name)

    return render_to_response("employeeInfo.html", Context({"userList": userList}))


def searchEm(request):
    """
    搜索员工,name,where,job,hobby
    :param request:
    :return:
    """
    query = request.GET.get("query")

    if query:
        qset = (Q(name__contains=query) |
                Q(where__contains=query) |
                Q(job__contains=query)   |
                Q(hobby__contains=query))

        userList = Employee.objects.filter(qset)
    else:
        userList = []

    return render_to_response("searchEmployeeInfo.html", Context({"userList": userList, "query": query}))


# 排除csrf装饰器
@csrf_exempt
@post
def searchEm2(request):
    """
    搜索员工,name,where,job,hobby
    :param request:
    :return:
    """
    print request.user
    if request.method == 'POST':
        form = QueryForm(request.POST)
        # 获取搜索关键字
        message = form.data['message']
        print message
    else:
        form = QueryForm()

    return render_to_response("searchEmployeeInfo2.html", Context({"form": form}))