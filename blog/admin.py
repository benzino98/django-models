from django.contrib import admin
from .models import Post


class PostDB(admin.ModelAdmin):
    list = [
        'title', 'text', 'author', 'created_date', 'published_date'
    ]
