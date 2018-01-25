# coding:utf-8
from django.db import models


class UserFileFolder(models.Model):
    '''
    用户文件夹
    '''
    id = models.AutoField(primary_key=True)
    userId = models.IntegerField()
    fileFolderName = models.CharField(u'文件夹名',max_length=255)
    createTime = models.DateTimeField(u'创建时间')
    deleted = models.IntegerField(u'是否已删除')
    deleteTime = models.DateTimeField(u'删除时间')

    def __str__(self):
        return '[' + self.id + ',' + self.userId + ',' + self.fileFolderName + ',' + self.createTime + ',' + self.deleted + ',' + self.deleteTime + ']'


class UserFile(models.Model):
    '''
    用户文件
    '''
    id = models.AutoField(primary_key=True)
    file_folder_id = models.IntegerField(u'所属文件夹id')
    fileName = models.CharField(u'文件名',max_length=255)
    createTime = models.DateTimeField(u'创建时间')
    deleted = models.IntegerField(u'是否已删除')
    deleteTime = models.DateTimeField(u'删除时间')
    fileSize = models.IntegerField(u'文件大小(kb)')

    def __str__(self):
        return '[' + self.id + ',' + self.file_folder_id + ',' + self.fileName + ',' + self.fileSize + ',' + self.createTime + ',' + self.deleted + ',' + self.deleteTime + ']'
