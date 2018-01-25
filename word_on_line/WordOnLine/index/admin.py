from django.contrib import admin
from index.models import UserFileFolder
from index.models import UserFile


class UserFileFolderAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'fileFolderName', 'createTime', 'deleteTime', 'deleted')
    list_filter = ('userId', 'fileFolderName', 'createTime', 'deleteTime', 'deleted')
    ordering = ('-createTime',)
    search_fields = ('userId', 'fileFolderName', 'createTime', 'deleteTime', 'deleted')


class UserFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'fileName', 'createTime', 'deleteTime', 'deleted', 'fileSize', 'file_folder_id')
    list_filter = ('fileName', 'createTime', 'deleteTime', 'deleted', 'fileSize', 'file_folder_id')
    ordering = ('-createTime',)
    search_fields = ('fileName', 'createTime', 'deleteTime', 'deleted', 'file_folder_id')


admin.site.register(UserFileFolder, UserFileFolderAdmin)
admin.site.register(UserFile, UserFileAdmin)