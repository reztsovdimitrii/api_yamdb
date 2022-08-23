from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, status, permissions
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from .serializers import (CategorySerializer, GenreSerializer,
                          TitleSerializer, ReviewSerializer, CommentSerializer,
                          RegisterUserSerializer, TokenSerialiser,
                          UserSerializer)
from .mixins import ListCreateDestroyViewSet
from .permissions import IsAdminOrReadOnly, IsAdmin, IsModerator, IsSuperuser

from reviews.models import Category, Genre, Title, Review, Comment, User
from reviews.utils import send_mail_to_user


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
    filterset_fields = ['category', 'genre', 'name']


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
        pk = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=pk)
        return review.comment.all()

    def perform_create(self, serializer):
        title = self.kwargs.get('title_id')
        review = self.kwargs.get('review_id')
        review = get_object_or_404(Review, title=title, pk=review)
        serializer.save(author=self.request.user, title=title, pk=review)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def register(request):
    serializer = RegisterUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username']
    )
    send_mail_to_user(user.email, user.confirmation_code)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def get_jwt_token(request):
    serializer = TokenSerialiser(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User,
        username=serializer.validated_data['username']
    )
    if user.confirmation_code == serializer.validated_data['confirmation_code']:
        token = AccessToken.for_user(user)
        return Response({"token": str(token)}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = "username"
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsAdmin | IsSuperuser,)

    @action(
        methods=[
            'get',
            'patch'
        ],
        detail=False,
        url_path='me',
        permission_classes=(permissions.IsAuthenticated,)
    )
    def get_or_update_self(self, request):
        if request.method == 'GET':
            serializer = self.get_serializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == 'PATCH':
            serializer = self.get_serializer(
                request.user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
