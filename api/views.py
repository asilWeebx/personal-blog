from rest_framework import generics
from .models import BlogPost, Author, Tags, Posts, Email, EmailS
from .serializers import BlogPostSerializer, AuthorSerializer, BlogPostPagination, TagsSerializer, PostsSerializer, \
    EmailSerializer, EmailSerializers


class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    pagination_class = BlogPostPagination

class AuthorListCreateView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class TagsListCreateView(generics.ListCreateAPIView):
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer

class PostsListCreateView(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class EmailListCreateView(generics.ListCreateAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer

class EmailSListCreateView(generics.ListCreateAPIView):
    queryset = EmailS.objects.all()
    serializer_class = EmailSerializers