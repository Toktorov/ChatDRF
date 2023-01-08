from django.shortcuts import render
from apps.chats.models import Chat, Message
from apps.chats.serializers import ChatSerializer
from rest_framework.generics import ListCreateAPIView

# Create your views here.
class ChatAPIView(ListCreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    # def perform_create(self, serializer):
    #     return serializer.save(from_chat_user = self.request.user)