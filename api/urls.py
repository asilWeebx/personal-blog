# urls.py
from django.urls import path
from .views import BlogPostListCreateView, AuthorListCreateView, TagsListCreateView, PostsListCreateView, \
    EmailListCreateView, EmailSListCreateView

urlpatterns = [
    path('api/blog/', BlogPostListCreateView.as_view(), name='blog-list-create'),
    path('api/author/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('api/tags/',TagsListCreateView.as_view(),name='tags-list-create'),
    path('api/posts/',PostsListCreateView.as_view(),name='posts-list-create'),
    path('api/emails/',EmailListCreateView.as_view(),name='emails-list-create'),
    path('api/email/',EmailSListCreateView.as_view(),name='email-list-create')
]
