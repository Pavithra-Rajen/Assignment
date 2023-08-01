from django.contrib import admin
from .models import *
#from petApp.models import ProductNew
# Register your models here.
class petAdmin(admin.ModelAdmin):
    list_display=['gender','image','species','name','breed','age','gender','description','price']
admin.site.register(petstore,petAdmin)
#admin.site.register(Pet)