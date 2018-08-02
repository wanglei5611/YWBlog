from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# 用户
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    nickname = models.CharField(max_length=32)
    email    = models.EmailField(max_length=64)

    def __str__(self):
        return '<UserInfo: %s>' % self.username

    class Meta:
        db_table = 'userinfo'
        verbose_name = '用户中心'
        verbose_name_plural = '用户中心'


# 博客类型
class BlogType(models.Model):
    type_name = models.CharField(max_length=32)

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 'blog_type'
        verbose_name = '博客类型'
        verbose_name_plural = '博客类型'


# 博客
class Blog(models.Model):
    title = models.CharField(max_length=70)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, to_field='id', on_delete=models.DO_NOTHING)
    blog_type = models.ForeignKey(BlogType, to_field='id', on_delete=models.DO_NOTHING)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Blog: %s>' % self.title

    class Meta:
        db_table = 'blog'
        verbose_name = '博客'
        verbose_name_plural = '博客'

