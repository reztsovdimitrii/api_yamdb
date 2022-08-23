from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, GenreViewSet,
                    TitleViewSet, ReviewViewSet, CommentViewSet, UserViewSet,
                    register, get_jwt_token)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register('genres', GenreViewSet, basename='genres')
router.register('titles', TitleViewSet, basename='titles')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token'),
]
# /categories/
# /categories/{slug}/
# /genres/
# /genres/{slug}/
# /titles/{titles_id}/
# /titles/{title_id}/reviews/
# /titles/{title_id}/reviews/{review_id}/
# /titles/{title_id}/reviews/{review_id}/comments/
# /titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
