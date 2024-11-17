from django.contrib import admin
from .import models

# Register your models here.


admin.site.register(models.Tag)

@admin.register(models.Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ['user','title','content','created_at','updated_at']
    search_fields = ['title']


@admin.register(models.Contact)
class AdminContact(admin.ModelAdmin):
    list_display =  ['name','email','subject','message']