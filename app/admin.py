from django.contrib import admin
from app.models import *

# Register your models here.

class BusinessAdmin(admin.ModelAdmin):
    list_display = ('com_name','pro_name','identify', 'host_name','exp_date')
    search_fields = ('com_name__com_name','identify')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pro_name', 'cost', 'price')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('com_name','con_name','email','tel','dep_name')
    search_fields = ('com_name',)

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Department)
admin.site.register(Business,BusinessAdmin)
