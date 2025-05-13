from django.contrib import admin
from .models import *

# Register your models here.

class product_data(admin.ModelAdmin):
    ordering = ["id"]
    list_display=["id","pname","price","qty","pimage"]

admin.site.register(product)
admin.site.register(product_detail,product_data)
