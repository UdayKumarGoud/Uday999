from django.contrib import admin
from . models import Employee

class EmployeAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'email_address', 'phone_number')
    
admin.site.register(Employee,EmployeAdmin)
