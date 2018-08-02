from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.blogList, name='home'),
    path('blog_list', views.blogList, name='blog_list'),
    path('blog_detail/<int:blog_id>/', views.blogDetail, name='blog_detail'),
    path('blog_type_list/<int:blog_type_id>/', views.blogTypeList, name='blog_type_list'),
    path('blog_author_list/<int:blog_author_id>/', views.blogAuthorList, name='blog_author_list'),
    path('blog_date_list/<int:year>/<int:month>/', views.blogDateList, name='blog_date_list'),
    path('blog_search_list/', views.blogSearchList, name='blog_search_list'),
]

