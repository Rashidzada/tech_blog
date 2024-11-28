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

@admin.register(models.FeedBack)
class AdminFeedBack(admin.ModelAdmin):
    list_display = ['name','title','content','data_file']

admin.site.register(models.News)


@admin.register(models.Student)
class AdminStudent(admin.ModelAdmin):
    list_display = ['name','eng','urd','total_marks','grade','percentage','remarks']

@admin.register(models.Info)
class AdminInfo(admin.ModelAdmin):
    list_display = ['first_name','last_name','full_name']