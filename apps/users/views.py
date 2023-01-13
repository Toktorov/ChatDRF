from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from apps.users.models import User
from apps.users.serializers import UserSerializer, UserRegisterSerializer, UserRetrieveUpdateDestroyAPIViewSerializer
from apps.users.permissions import IsUserPermissions
from rest_framework.response import Response
import datetime

# Create your views here.
class UserAPIViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, )

class UserRegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveUpdateDestroyAPIViewSerializer
    permission_classes = (IsUserPermissions, )

    def get(self, request, pk):
        user = User.objects.get(pk = pk)
        if request.user == user:
            user.last_activity = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            user.save()
        serializer = UserRetrieveUpdateDestroyAPIViewSerializer(user)
        return Response({'user' : serializer.data} )