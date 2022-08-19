from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Titles(models.Model):
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE,
        related_name='category', blank=True, null=True)
    genre = models.ManyToManyField(Genres, blank=True,
                                   related_name='title')
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()


class Review(models.Model):
    slug = models.SlugField(max_length=50)
    text = models.TextField()
    score = models.IntegerField()
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')
    title = models.ForeignKey(
        Titles, on_delete=models.CASCADE,
        related_name='title', blank=True, null=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)


class Comments(models.Model):
    slug = models.SlugField(max_length=50)
    text = models.TextField()
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
