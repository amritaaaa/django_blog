from django.conf.urls import url
from django.contrib import admin
from . import views
from blogger.views import home,blog_detail

urlpatterns = [
    url(r'^$', views.home ,name="home"),
    url(r'(?P<blog_id>\d+)$', views.blog_detail),
    url(r'^registration',views.register , name='register'),
    url(r'^loginn',views.login , name='login'),
    url(r'^create_blog',views.create_blog,name='create_blog')
]

