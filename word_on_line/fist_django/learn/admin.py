from django.contrib import admin
from models import *

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'sex', 'where', 'job', 'hobby')
    list_filter = ('name', 'age', 'sex', 'where', 'job', 'hobby')
    ordering = ('-age',)
    search_fields = ('name', 'where', 'hobby')


admin.site.register(Employee, EmployeeAdmin)
