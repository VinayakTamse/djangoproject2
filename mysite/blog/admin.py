from django.contrib import admin
from blog.models import BlogPosts, BlogComments

# Register your models here.

admin.site.register((BlogPosts, BlogComments))
