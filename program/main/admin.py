from django.contrib import admin

from .models import Book, Tag, Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'created', )
	prepopulated_fields = {'slug': ('title', )}
	search_fields = ('title', 'body', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', )
	prepopulated_fields = {'slug': ('name', )}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', )
	prepopulated_fields = {'slug': ('name', )}