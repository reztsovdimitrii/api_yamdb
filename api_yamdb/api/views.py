from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from django.shortcuts import get_object_or_404

from .serializers import CategorySerializer, GenreSerializer, TitleSerializer, ReviewSerializer, CommentSerializer
from .mixins import ListCreateDestroyViewSet
from reviews.models import Category, Genre, Title, Review, Comment


class CategoryViewSet(ListCreateDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes = AdminOrReadOnly
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(ListCreateDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # permission_classes = AdminOrReadOnly
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    # permission_classes = AdminOrReadOnly
    filter_backends = [DjangoFilterBackend]
    # filter_class = ???


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    # premission_classes = AuthorModeratorOrAdmin

    def get_queryset(self):
        pk = self.kwargs.get('title_id')
        title = get_object_or_404(Title, pk=pk)
        return title.reviews.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('title_id')
        title = get_object_or_404(Title, pk=pk)
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    # permission_classes = AuthorModeratorOrAdmin

    def get_queryset(self):
        pk=self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=pk)
        return review.comment.all()

    def perform_create(self, serializer):
        title = self.kwargs.get('title_id')
        review = self.kwargs.get('review_id')
        review = get_object_or_404(Review, title=title, pk=review)
        serializer.save(author=self.request.user, title=title, pk=review)
