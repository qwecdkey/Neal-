from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import teacherChart
# Register your models here.

class teacherChartInline(admin.TabularInline):
    model = teacherChart
    can_delete = False
    can_delete_plural = 'TeacherChart'
    
class UserAdmin(BaseUserAdmin):
    inlines = (teacherChartInline, )
    
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
