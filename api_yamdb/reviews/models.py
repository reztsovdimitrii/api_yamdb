from unicodedata import name
from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50)


class Genres(models.Model):
    search = models.CharField(max_length=256)


class Titles(models.Model):
    category = 
    genre = 
    name = 
    year = 
    description = models.TextField()


class Review(models.Model):


class Comments(models.Model):

