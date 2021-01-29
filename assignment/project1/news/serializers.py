from rest_framework import serializers
from .models import News


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['kind', 'title', 'author', 'display']