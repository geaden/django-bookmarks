import os.path

from django.views.generic.simple import direct_to_template
from django.conf.urls import patterns, include, url
from bookmarks.views import *
from bookmarks.feeds import *

site_media = os.path.join(os.path.dirname(__file__), 'site_media')

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

feeds = {
        'recent': RecentBookmarks,
        'user': UserBookmarks
        }

urlpatterns = patterns('',
    #i18n
    (r'^i18n/', include('django.conf.urls.i18n')),

    #Feeds
    (r'^feeds/recent/$', RecentBookmarks()),
    (r'^feeds/user/(?P<username>\w+)/$', UserBookmarks()),

    #Friends
    (r'^friends/(\w+)/$', friend_page),
    (r'^friend/add/$', friend_add),
    (r'^friend/invite/$', friend_invite),
    (r'^friend/accept/(\w+)/$', friend_accept),

    #Ajax
    (r'^ajax/tag/autocomplete/$', ajax_tag_autocomplete),
    
    #Comments
    (r'^comments/', include('django.contrib.comments.urls')),

    #Admin interface
    url(r'^admin/', include(admin.site.urls)),

    #Browsing
    (r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
    (r'^tag/([^\s]+)/$', tag_page),
    (r'^tag/$', tag_cloud_page),
    (r'^popular/$', popular_page),
    (r'^bookmark/(\d+)/$', bookmark_page),
    
    #Session management
    (r'^login/$','django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^register/$', register_page),
    (r'^register/success/$', direct_to_template, {'template':'registration/register_success.html' }),
      
    #Static
    (r'^site_media/(?P<path>.*)$','django.views.static.serve', {'document_root': site_media }),
    
    #Account management
    (r'^save/$', bookmark_save_page),
    (r'^vote/$', bookmark_vote_page),

    #Search
    (r'^search/$', search_page),
    
    # Examples:
    # url(r'^$', 'django_bookmarks.views.home', name='home'),
    # url(r'^django_bookmarks/', include('django_bookmarks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
