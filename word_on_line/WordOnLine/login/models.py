# coding:utf-8
from django.db import models


class UserLoginRecord(models.Model):
    '''
    用户登录记录表
    '''
    id = models.AutoField(primary_key=True)
    userId = models.IntegerField()
    loginTime = models.DateTimeField()
    status = models.IntegerField()

    def __str__(self):
        return '[' + self.id + ',' + self.userId + ',' + self.loginTime + ',' + self.status  + ']'

