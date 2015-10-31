from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url(r'^ajax_login/', views.ajax_login, name='ajax_login'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^add_page/', views.add_page, name='add_page'),
    url(r'^add_record/', views.add_record, name='add_record'),
    url(r'^add_disease/', views.add_disease, name='add_disease'),
    url(r'^add_event/', views.add_event, name='add_event'),
    url(r'^add_review/', views.add_review, name='add_review'),
    url(r'^$', views.register, name='index'),
)
