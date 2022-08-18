from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50)


class Genres(models.Model):
    search = models.CharField(max_length=256)


class Titles(models.Model):
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE,
        related_name='category', blank=True, null=True)
    genre = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    year = models.IntegerField()
    description = models.TextField()


class Review(models.Model):
    slug = models.SlugField(max_length=50)

class Comments(models.Model):
    slug = models.SlugField(max_length=50)
