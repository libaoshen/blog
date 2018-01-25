from django.contrib import admin
from login.models import UserLoginRecord
from index.models import UserFileFolder


# Register your models here.
class UserLoginRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'loginTime', 'status')
    list_filter = ('userId', 'loginTime', 'status')
    ordering = ('-loginTime',)
    search_fields = ('userId', 'loginTime', 'status')


class UserFileFolderAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'fileFolderName', 'createTime', 'deleteTime', 'deleted')
    list_filter = ('userId', 'fileFolderName', 'createTime', 'deleteTime', 'deleted')
    ordering = ('-createTime',)
    search_fields = ('userId', 'fileFolderName', 'createTime', 'deleteTime', 'deleted')


admin.site.register(UserLoginRecord, UserLoginRecordAdmin)
admin.site.register(UserFileFolder, UserFileFolderAdmin)