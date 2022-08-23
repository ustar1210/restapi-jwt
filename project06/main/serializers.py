from xml.etree.ElementTree import Comment
from rest_framework import serializers
from .models import *

class ReviewListSerializer(serializers.ModelSerializer):
    movie_id = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


