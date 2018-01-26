# coding:utf-8
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.template import Context
from login.forms import LoginForm
from django.contrib import auth
from login.models import UserLoginRecord
from datetime import datetime
from django.http import HttpResponseRedirect
from index.models import UserFileFolder

def toLogin(request):
    form = LoginForm()

    return render_to_response("login.html", {})


@csrf_exempt
def login(request):
    """
        搜索员工,name,where,job,hobby
        :param request:
        :return:
        """
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # 获取搜索关键字
        username = form.data['username']
        password = form.data['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            request.session['userName'] = user.username
            request.session['userId'] = user.id
            userLoginRecord = UserLoginRecord(userId=user.id, loginTime=datetime.now(), status=1)
            userLoginRecord.save()
            # 创建默认文件夹
            if UserFileFolder.objects.filter(fileFolderName=u'默认文件夹') is None:
                userFileFolder = UserFileFolder(userId=user.id, fileFolderName=u'默认文件夹', createTime=datetime.now(), deleted=0)
                userFileFolder.save()

            return HttpResponseRedirect('/index/0')
        else:
            message = '账号或密码不正确'
            return render_to_response("login.html", Context({"form2": form, "message": message}))
    else:
        form = LoginForm()
        form.message = '只支持POST登录'

    return render_to_response("login.html", Context({"form2": form}))

def logout(request):
    if request.session.has_key('userId') and request.session['userId'] is not None:
        request.session['userId'] = None
        return HttpResponseRedirect('/login')
