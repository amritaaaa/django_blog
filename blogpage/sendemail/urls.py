from django.conf.urls import url
#from django.contrib import admin
from . import views
from .views import sendmail

urlpatterns = [
    url(r'^$', views.sendmail),

]

