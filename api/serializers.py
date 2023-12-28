# serializers.py
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination

from .models import BlogPost, Author, Tags, Posts, Email, EmailS


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'bio', 'profile_image')

class BlogPostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'text', 'blog_image', 'hashtags', 'author', 'date','url','url_name')

class BlogPostPagination(PageNumberPagination):
    page_size = 5  # Sizning xohlagan sahifadagi blog postlar soni

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('id','name','tag_image')

class PostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('id','post_images','title','text','hashtags','tips')

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['id', 'recipient', 'sent_at']

class EmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmailS
        fields = ['id', 'name', 'recipient', 'sent_at']

