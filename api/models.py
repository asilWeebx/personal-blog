# models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='author_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    url = models.URLField(max_length=120,blank=True,null=True)
    url_name = models.CharField(max_length=150,blank=True,null=True)
    blog_image = models.ImageField(upload_to='blog_images/')
    hashtags = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Tags(models.Model):
    name = models.CharField(max_length=250)
    tag_image = models.ImageField(upload_to='tag_image/')

    def __str__(self):
        return self.name


class Posts(models.Model):
    post_images = models.ImageField(upload_to='recent/')
    title = models.CharField(max_length=250)
    text = models.TextField(max_length=250)
    hashtags = models.CharField(max_length=250)
    tips = models.CharField(max_length=250)

    def __str__(self):
        return self.title

class Email(models.Model):
    recipient = models.EmailField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.recipient


class EmailS(models.Model):
    recipient = models.EmailField(unique=True)
    name = models.CharField(max_length=250)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name