from django.shortcuts import render
from .models import Author, Blog
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import AuthorSerializer, BlogSerializer, UserSerializer, GroupSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class AuthorViewSet(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BlogViewSet(viewsets.ModelViewSet):

    queryset = Blog.objects.all().order_by('created_at')
    serializer_class = BlogSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LoginView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth),
        }
        return Response(content)

def home(request):
    return render(request, 'index.html')
