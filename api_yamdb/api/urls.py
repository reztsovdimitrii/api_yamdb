from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, GenreViewSet,
                    TitleViewSet, ReviewViewSet, CommentViewSet)

router = DefaultRouter()

router.register('categories', CategoryViewSet, basename='category')
router.register('genres', GenreViewSet, basename='genre')
router.register('titles', TitleViewSet, basename='title')
router.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet, basename='review')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comment'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
    # /categories/
    # /categories/{slug}/
    # /genres/
    # /genres/{slug}/
    # /titles/{titles_id}/
    # /titles/{title_id}/reviews/
    # /titles/{title_id}/reviews/{review_id}/
    # /titles/{title_id}/reviews/{review_id}/comments/
    # /titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
]
