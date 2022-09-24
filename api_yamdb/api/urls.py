from django.urls import include, path
from rest_framework import routers

from api import views

v1_router = routers.DefaultRouter()
v1_router.register(r'categories', views.CategoryViewSet)
v1_router.register(r'genres', views.GenreViewSet)
v1_router.register(r'titles', views.TitleViewSet)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    views.ReviewViewSet, basename='review'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet, basename='comment'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
