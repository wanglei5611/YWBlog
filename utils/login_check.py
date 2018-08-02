from functools import wraps
from django.shortcuts import redirect, reverse

# 登陆验证装饰器
def login_check(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        if not request.session.get('username'):
            return redirect(reverse('login'))
        return func(request, *args, **kwargs)
    return inner
