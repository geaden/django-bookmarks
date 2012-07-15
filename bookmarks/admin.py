from bookmarks.models import Bookmark, Tag, Link, SharedBookmark, Friendship, Invitation
from django.contrib import admin

class BookmarkAdmin(admin.ModelAdmin):
    fields = ['title', 'link', 'user']
    list_display = ('title', 'link', 'user')
    list_filter = ('user', )
    ordering = ('title', )
    search_fields = ('title', )

admin.site.register(Bookmark, BookmarkAdmin)

admin.site.register(Tag)
admin.site.register(Link)
admin.site.register(SharedBookmark)

class FriendshipAdmin(admin.ModelAdmin):
	list_filter = ('from_friend', )

admin.site.register(Friendship, FriendshipAdmin)

class InvitationAdmin(admin.ModelAdmin):
	ordering = ('email', )

admin.site.register(Invitation, InvitationAdmin)