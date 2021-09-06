# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny

from loud9ja.models import CustomUser
from loud9ja.serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
