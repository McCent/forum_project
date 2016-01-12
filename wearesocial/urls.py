"""wearesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from accounts.views import register, login, logout, profile, subscriptions_webhook
from threads.views import threads, new_thread, thread, new_post, edit_post, delete_post, forum
import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'core.views.get_index', name='home'),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^contact/', 'contact.views.contact', name='contact'),
    url(r'^register/$', register, name='register'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^forum/$', forum, name='forum'),
    url(r'^accounts/subscriptions/$', subscriptions_webhook, name='subscriptions'),
    url(r'^threads/(?P<subject_id>\d+)/$', threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', edit_post, name='edit_post'),
    url(r'^post/delete_post/(?P<post_id>\d+)/$', delete_post, name='delete_post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)