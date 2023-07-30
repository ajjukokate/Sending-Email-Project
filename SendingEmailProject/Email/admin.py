from django.contrib import admin
from .models import Employee

# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','emp_id','name','birthdate','work_anniversary_date','email']

admin.site.register(Employee,EmployeeAdmin)
