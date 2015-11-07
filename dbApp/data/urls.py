from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    # url(r'^ajax_login/', views.ajax_login, name='ajax_login'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^dashboard/page', views.edit_page_contact, name='edit_page_contact'),
    url(r'^event/add/$', views.add_event, name='add_event'),
    url(r'^event/(?P<id>[0-9]+)/edit/$', views.edit_event, name='edit_event'),
    url(r'^event/(?P<event_id>[0-9]+)/add/$', views.add_record, name='add_record'),
    url(r'^event/(?P<event_id>[0-9]+)/(?P<id>[0-9]+)/$', views.add_record, name='edit_record'),
    url(r'^event/(?P<id>[0-9]+)/$', views.event_detail, name='event_detail'),
    url(r'^page/add', views.add_page, name='add_page'),
    url(r'^page/(?P<page_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
    # url(r'^page/(?P<page_id>[0-9]+)/(?P<id>[0-9]+)/$', views.add_review, name='edit_review'),
    url(r'^page/(?P<id>[0-9]+)/$', views.page_detail, name='page_detail'),
    url(r'^page/(?P<id>[0-9]+)/edit$', views.edit_page_contact, name='edit_page'),
    url(r'^page/$', views.page_list, name='page_list'),
    url(r'^disease/add/$', views.add_disease, name='add_disease'),
    url(r'^disease/(?P<id>[0-9]+)/$', views.edit_disease, name='edit_disease'),
    url(r'^$', views.register, name='index'),
)
