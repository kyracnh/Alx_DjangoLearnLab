from django.urls import path, include
from .views import BookListAPIView, BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Router for BookViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    # Map the BookListAPIView to the /books-list/ URL
    path('books-list/', BookListAPIView.as_view(), name='book-list'),
    
    # Include all router-generated URLs
    path('', include(router.urls)),
    
    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
