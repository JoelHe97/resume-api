from rest_framework import generics, views
from apps.users.models import User
from .serializers import UserSerializer


class ProfileView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
