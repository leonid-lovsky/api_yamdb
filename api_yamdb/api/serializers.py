from django.contrib.auth import get_user_model
from rest_framework import serializers

from reviews import models

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('name', 'slug',)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = ('name', 'slug',)


class TitleSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField()
    description = serializers.CharField(
        allow_blank=True, required=False
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug', required=True, many=True,
        queryset=models.Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug', required=True,
        queryset=models.Category.objects.all()
    )

    class Meta:
        model = models.Title
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category',
        )
        read_only_fields = ('rating',)

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['genre'] = GenreSerializer(instance.genre, many=True).data
        response['category'] = CategorySerializer(instance.category).data
        return response
