# coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from index.models import UserFile
from index.models import UserFileFolder

def toIndex(request, fileFolderId):
    if request.session.has_key('userId') and request.session['userId'] is not None:
        # 获取userId
        userId = request.session['userId']
        # 获取对应的文件夹和文件
        fileFolderId = int(fileFolderId)
        userFileFolder = None
        userFile = None
        if fileFolderId == 0:
            userFileFolder = UserFileFolder.objects.filter(userId=userId)
        else:
            userFile = UserFile.objects.filter(file_folder_id=fileFolderId)

        return render_to_response('index.html', {"username": request.session['userName'], "userFileFolder": userFileFolder, "userFile": userFile})
    else:
        return HttpResponseRedirect('/login')