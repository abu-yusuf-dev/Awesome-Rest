from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Author, Blog
from django.contrib.auth.validators import UnicodeUsernameValidator


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
            },
            'username': {
                 'validators': [UnicodeUsernameValidator()],
            },
        }


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
