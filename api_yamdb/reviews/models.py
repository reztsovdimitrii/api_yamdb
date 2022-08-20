from django.contrib.auth import get_user_model

from django.db import models

User = get_user_model()


class Categories(models.Model):
    """Класс для представления списка категорий:
    «Книги», «Фильмы», «Музыка». Может быть расширен администратором.
    """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genres(models.Model):
    """Класс для представления жанра из списка предустановленных.
    Новые жанры может создавать только администратор.
    """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Titles(models.Model):
    """Класс для представления произведений."""
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE,
        related_name='category', blank=True, null=True)
    genre = models.ManyToManyField(Genres, blank=True,
        related_name='title')
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):
    """Класс для представления отзывов и
    оценок на произведения titles от пользователей.
    """
    slug = models.SlugField(max_length=50)
    text = models.TextField()
    score = models.IntegerField()
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='review')
    title = models.ForeignKey(
        Titles, on_delete=models.CASCADE,
        related_name='title', blank=True, null=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text


class Comments(models.Model):
    """Класс для представления комментариев к отзывам."""
    slug = models.SlugField(max_length=50)
    text = models.TextField()
    #author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text
