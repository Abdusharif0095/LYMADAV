from django.contrib import admin
from .models import *


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_id', 'user_id', 'title', 'created_at', 'updated_at', 'is_published', 'is_reviewed')
    list_display_links = ('id', 'category_id', 'user_id', 'title', 'created_at', 'updated_at', 'is_published', 'is_reviewed')
    search_fields = ('title', 'content')


class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'position_id', 'fullname', 'email', 'password', 'birthday', 'about', 'status')
    links_display = ('id', 'position_id', 'fullname', 'email', 'password', 'birthday', 'about', 'status')
    search_fields = ('fullname', 'email')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'news_id', 'writer', 'content', 'time', 'is_published')
    list_display_links = ('id', 'news_id', 'writer', 'content', 'time', 'is_published')
    search_fields = ('writer', 'content')


admin.site.register(News, NewsAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Comment, CommentAdmin)
