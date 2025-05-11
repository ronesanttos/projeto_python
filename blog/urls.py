from django.urls import path
from django.http import HttpResponse

from blog import views as views_blog

app_name = 'blog'

urlpatterns = [
    path('', views_blog.blog,name='home'),
    path('exemple/', views_blog.exemple,name='exemple')
]
