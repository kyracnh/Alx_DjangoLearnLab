from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookListAPIView, BookViewSet

# Router for the ViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('books-list/', BookListAPIView.as_view(), name='book-list'),  # List API view
    path('', include(router.urls)),  # Routes for the ViewSet
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),  # Token auth
]
