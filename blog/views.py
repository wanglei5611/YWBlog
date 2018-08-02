from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from blog import forms
from blog import models
from django.contrib import auth
from utils.page_public import getPublicAllList
from utils.login_check import login_check

# 模板中上下文使用
def context_func(request):
    context = {}
    context['SITE_NAME'] = settings.SITE_NAME
    return context


# 登陆页
def login(request):
    if request.method == 'GET':
        loginform = forms.LoginForm()
        return render(request, 'blog/login.html', {'loginform': loginform})
    elif request.method == 'POST':
        loginform = forms.LoginForm(request.POST)
        if loginform.is_valid():
            # 使用django的用户
            obj = auth.authenticate(username=loginform.cleaned_data.get('username'), password=loginform.cleaned_data.get('password'))
            #obj = models.UserInfo.objects.filter(**loginform.cleaned_data).first()
            if obj:
                request.session['username'] = loginform.cleaned_data.get('username')
                return redirect(reverse('blog_list'))
            else:
                error_message = '用户名或密码错误'
                return render(request, 'blog/login.html', {'loginform': loginform,'error_message': error_message})
        else:
            return render(request, 'blog/login.html', {'loginform': loginform})



# 注销登陆
@login_check
def logout(request):
    request.session.pop('username')
    return redirect(reverse('login'))


# 博客列表
@login_check
def blogList(request):
    blog_all_list = models.Blog.objects.all()
    context = getPublicAllList(request, blog_all_list)
    return render(request, 'blog/blog_list.html', context)


# 博客详情
@login_check
def blogDetail(request, blog_id):
    context = {}
    context['blog'] = get_object_or_404(models.Blog, id=blog_id)
    return render(request, 'blog/blog_detail.html', context)


# 博客分类列表
@login_check
def blogTypeList(request, blog_type_id):
    blog_type = get_object_or_404(models.BlogType, id=blog_type_id)
    blog_type_list = models.Blog.objects.filter(blog_type=blog_type)
    context = getPublicAllList(request, blog_type_list)
    return render(request, 'blog/blog_type_list.html', context)


# 博客作者分类
@login_check
def blogAuthorList(request, blog_author_id):
    blog_author = get_object_or_404(models.User, id=blog_author_id)
    blog_author_list = models.Blog.objects.filter(author=blog_author)
    context = getPublicAllList(request, blog_author_list)
    return render(request, 'blog/blog_author_list.html', context)


# 博客日期分类
@login_check
def blogDateList(request, year, month):
    # 分页逻辑
    blog_all_list = models.Blog.objects.filter(create_time__year=year, create_time__month=month)
    context = getPublicAllList(request, blog_all_list)
    context['blog_date'] = '%s年%s月' % (year, month)
    return render(request, 'blog/blog_date_list.html', context)


# 搜索博客
def blogSearchList(request):
    wd = request.GET.get('wd')
    if not wd:
        return redirect(reverse('blog_list'))
    blog_all_list = models.Blog.objects.filter(title__contains=wd)
    context = getPublicAllList(request, blog_all_list)
    print(context)
    return render(request, 'blog/blog_search.html', context)
