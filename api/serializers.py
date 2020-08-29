from rest_framework import serializers
from articles.models import Article, Comment
from users.models import CustomUser


class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'body', 'author')


class UpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'body', 'author')


class DetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'body', 'author')

class CreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('title', 'body', 'author')


class CreateUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'id')

