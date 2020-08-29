from django.urls import path

from .views import NewsAPIView, UpdateArticleAPIView, DetailArticleAPIView, CreateArticleAPIView, CreateUserAPIView

urlpatterns = [
    path('', NewsAPIView.as_view()),
    path('update/', UpdateArticleAPIView.as_view()),
    path('<int:pk>/', DetailArticleAPIView.as_view()),
    path('new/', CreateArticleAPIView.as_view()),
    path('signups/', CreateUserAPIView.as_view()),
]