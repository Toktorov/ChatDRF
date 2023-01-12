from django.shortcuts import render
from apps.chats.models import Chat, Message
from apps.chats.serializers import ChatSerializer, ChatChatRetrieveSerializer, MessageCreateSerializer
from apps.chats.permissions import ChatPermissions
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.db.models import Q

# Create your views here.
class ChatAPIView(ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Chat.objects.filter(Q(from_chat_user = self.request.user)|Q(to_chat_user = self.request.user))

    def perform_create(self, serializer):
        return serializer.save(from_chat_user = self.request.user)

class ChatRetrieveAPIView(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatChatRetrieveSerializer
    permission_classes = (ChatPermissions, )

class ChatDestroyAPIView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (ChatPermissions, )

class ChatMessageCreateAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCreateSerializer

class ChatMessageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCreateSerializer