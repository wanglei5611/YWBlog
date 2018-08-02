from blog import models
from django.core.paginator import Paginator
from django.db.models import Count

# 博客公共代码
def getPublicAllList(request, blog_all_list):
    # 分页逻辑
    paginator = Paginator(blog_all_list, 10)
    page_num = request.GET.get('page', default=1)
    current_page = paginator.get_page(page_num)
    page_range = list(range(max(current_page.number - 2, 1), current_page.number)) + list(
        range(current_page.number, min(paginator.num_pages, current_page.number + 2) + 1))

    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    blog_dates = models.Blog.objects.dates('create_time', 'month', order='DESC')
    blog_dates_dict = {}
    for blog_date in blog_dates:
        blog_count = models.Blog.objects.filter(create_time__year=blog_date.year, create_time__month=blog_date.month).count()
        blog_dates_dict[blog_date] = blog_count

    context = {}
    context['total'] = blog_all_list.count()
    context['page_range'] = page_range
    context['current_page'] = current_page
    context['blogs'] = current_page.object_list
    context['blog_types'] = models.BlogType.objects.annotate(blog_count_num=Count('blog'))
    context['blog_dates'] = blog_dates_dict
    return context
