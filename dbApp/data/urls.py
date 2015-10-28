from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^ajax_login/', views.ajax_login, name='ajax_login'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^add_page/', views.add_page, name='add_page'),
    url(r'^$', views.register, name='index'),
)
