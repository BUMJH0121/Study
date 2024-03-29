from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from blog.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date-joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]