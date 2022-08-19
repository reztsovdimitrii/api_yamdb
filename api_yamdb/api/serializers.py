from rest_framework import serializers

from reviews.models import Categories, Genres, Titles, Review, Comments


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Categories


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genres


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Titles


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Comments
