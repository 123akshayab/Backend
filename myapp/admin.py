from django.contrib import admin
from rest_framework.authtoken.admin import TokenAdmin
from myapp.models import Employee

# Register your models here.

TokenAdmin.raw_id_fields = ['user']

admin.site.register(Employee)