from rest_framework import generics
from .serializers import NewsSerializers, UpdateSerializers, DetailSerializers, CreateSerializers, CreateUserSerializers
from articles.models import Article
from users.models import CustomUser


# Create your views here.
class NewsAPIView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = NewsSerializers


class UpdateArticleAPIView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = UpdateSerializers


class DetailArticleAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = DetailSerializers


class CreateArticleAPIView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = CreateSerializers


class CreateUserAPIView(generics.CreateAPIView):
    queryset = CustomUser
    serializer_class = CreateUserSerializers
