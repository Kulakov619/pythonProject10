from django.contrib import admin
from authcore import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user_to', 'user_from')


class AlbumInline(admin.StackedInline):
    model = models.Album
    exclude = ('id',)
    extra = 0


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    inlines = [AlbumInline, ]
    list_display = ('email', 'username')
    search_fields = ('email', 'username')


class PhotoInline(admin.StackedInline):
    model = models.Photo
    exclude = ('id',)
    extra = 0


@admin.register(models.Album)
class UserAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]
    list_display = ('name', 'user')
    search_fields = ('name', 'user')