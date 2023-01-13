from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from apps.users.models import User
from apps.users.serializers import UserSerializer, UserRegisterSerializer, UserRetrieveUpdateDestroyAPIViewSerializer
from apps.users.permissions import IsUserPermissions
from apps.chats.models import Chat
from django.db.models import Q
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

class UsersAnotherAPIView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        chats = Chat.objects.filter(Q(from_chat_user = self.request.user)|Q(to_chat_user = self.request.user))
        users_id = list(chats.values_list('from_chat_user', flat=True)) + list(chats.values_list('to_chat_user', flat=True))
        users_id.append(self.request.user.id)
        users = User.objects.exclude(id__in=users_id)
        return users