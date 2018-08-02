from django.contrib import admin
from blog import models


@admin.register(models.UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['username', 'nickname', 'email']


@admin.register(models.BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name', ]


@admin.register(models.Blog)
class Blog(admin.ModelAdmin):
    list_display = ['title', 'author', 'blog_type', 'create_time', 'update_time', ]

