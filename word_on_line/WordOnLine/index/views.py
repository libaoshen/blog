# coding:utf-8
from django.shortcuts import render_to_response


def toIndex(request):
    return render_to_response('index.html', {})