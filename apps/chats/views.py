from django.shortcuts import render
from apps.chats.models import Chat, Message
from apps.chats.serializers import ChatSerializer, ChatChatRetrieveSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView

# Create your views here.
class ChatAPIView(ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    # def perform_create(self, serializer):
    #     return serializer.save(from_chat_user = self.request.user)

class ChatRetrieveAPIView(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatChatRetrieveSerializer