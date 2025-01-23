from django.contrib import admin

# Register your models here. una vez hechos los modelos, debemos registrarlos en el admin

from django.contrib import admin
from .models import Post, Category, Tag, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_published')
    search_fields = ('title', 'content', 'author__username')
    list_filter = ('is_published', 'categories', 'tags')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at', 'is_approved')
    search_fields = ('user__username', 'post__title', 'content')
    list_filter = ('is_approved',)
