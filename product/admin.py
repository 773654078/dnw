from django.contrib import admin
from .models import productItems
# Register your models here.

#产品录入

class productAamin(admin.ModelAdmin):
    search_fields = ['pName']
    list_display = ['pName', 'pprice', 'pnumber']

admin.site.register(productItems, productAamin)