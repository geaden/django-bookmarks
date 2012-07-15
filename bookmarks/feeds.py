from django.contrib.syndication.views import Feed
from bookmarks.models import Bookmark
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.syndication.views import FeedDoesNotExist
from django.shortcuts import get_object_or_404

class RecentBookmarks(Feed):
	title = 'Django Bookmarks | Recent Bookmarks'
	link = '/feed/recent'
	description = 'Recent bookmarks posted to Django Bookmarks'
	description_template = 'feeds/recent_description.html'
	title_template = 'feeds/recent_title.html'

	def items(self):
		return Bookmark.objects.order_by('-id')[:10]
 

class UserBookmarks(Feed):
	description_template = 'feeds/user_description.html'
	title_template = 'feeds/user_title.html'

 	def get_object(self, request, username):
 		return get_object_or_404(User, username=username)


 	def title(self, user):
 		return 'Django Bookmarks | Bookmarks for %s' % user.username


 	def link(self, user):
 		return '/feeds/user/%s/' % user.username

 	def description(self, user):
 		return 'Recent bookmarks posted by %s' % user.username

 	def items(self, user):
 		return user.bookmark_set.order_by('-id')[:10]