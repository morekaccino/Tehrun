from django.contrib.auth.models import User
from django.db import models
from meta.models import ModelMeta

# Create your models here.
from django.urls import reverse


class IndexPage(models.Model):
    page = models.IntegerField(unique=True, primary_key=True)


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=1000)
    body = models.TextField()
    is_english = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])