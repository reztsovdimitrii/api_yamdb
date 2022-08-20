from django.db import models
from django.contrib.auth.models import AbstractUser

from .utils import generate_confirmation_code


class User(AbstractUser):

    admin = 'admin'
    moderator = 'moderator'
    user = 'user'
    CHOICES = (
        (admin, 'admin'),
        (moderator, 'moderator'),
        (user, 'user'),
    )

    bio = models.TextField(blank=True, verbose_name='Информация о себе')
    role = models.CharField(
        max_length=50,
        null=True,
        choices=CHOICES,
        verbose_name='Роль'
    )
    username = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        unique=True
    )
    email = models.EmailField(
        max_length=255,
        blank=False,
        null=False,
        unique=True
    )
    confirmation_code = models.CharField(
        max_length=100,
        null=True,
        verbose_name='Код подтверждения',
        default=generate_confirmation_code
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Category(models.Model):
    """Класс для представления списка категорий:
    «Книги», «Фильмы», «Музыка». Может быть расширен администратором.
    """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    """Класс для представления жанра из списка предустановленных.
    Новые жанры может создавать только администратор.
    """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    """Класс для представления произведений."""
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='titles',
        blank=True,
        null=True)
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        related_name='titles')
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.name


class Review(models.Model):
    """Класс для представления отзывов и
    оценок на произведения titles от пользователей.
    """
    text = models.TextField()
    score = models.IntegerField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        blank=True,
        null=True
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'], name='unique_review')
        ]

    def __str__(self):
        return self.text


class Comment(models.Model):
    """Класс для представления комментариев к отзывам."""
    slug = models.SlugField(max_length=50)
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Отзыв'
    )
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.text
