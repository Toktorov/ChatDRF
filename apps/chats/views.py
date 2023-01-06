from django.shortcuts import render
from apps.chats.models import Chat, Message
from apps.chats.serializers import ChatSerializer
from rest_framework.generics import ListAPIView

# Create your views here.
class ChatAPIView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer