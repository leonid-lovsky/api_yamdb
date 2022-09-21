from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)


class Title(models.Model):
    name = models.CharField(max_length=256)
    year = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    genre = models.ManyToManyField(Genre, related_name='titles')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name='titles', null=True)
