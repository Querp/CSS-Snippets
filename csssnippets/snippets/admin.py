from django.contrib import admin
from .models import Snippet, SnippetBody


class SnippetBodyInline(admin.TabularInline):
    model = SnippetBody
    extra = 1
    ordering = ('order',)
    fields = ('order', 'block_type', 'language', 'content')


@admin.register(Snippet)
class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')
    inlines = [SnippetBodyInline]


@admin.register(SnippetBody)
class SnippetBodyAdmin(admin.ModelAdmin):
    list_display = ('snippet', 'block_type', 'language', 'order')
    list_filter = ('block_type', 'language')
    ordering = ('snippet', 'order')
