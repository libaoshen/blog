from django.contrib import admin
from login.models import UserLoginRecord

# Register your models here.


class UserLoginRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'userId', 'loginTime', 'status')
    list_filter = ('userId', 'loginTime', 'status')
    ordering = ('-loginTime',)
    search_fields = ('userId', 'loginTime', 'status')


admin.site.register(UserLoginRecord, UserLoginRecordAdmin)
