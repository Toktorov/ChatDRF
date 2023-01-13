from apps.chats.models import Chat, Message
from apps.chats.serializers import ChatSerializer, ChatChatRetrieveSerializer, MessageCreateSerializer
from apps.chats.permissions import ChatPermissions
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from rest_framework.response import Response

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
    
    def get(self, request, pk):
        chat = Chat.objects.get(pk = pk)
        message = Message.objects.filter(chat = chat.id, to_user = request.user)
        for mes in message:
            mes.is_read = True 
            mes.save()
        serializer = ChatChatRetrieveSerializer(chat)
        return Response({'message' : serializer.data} )

class ChatDestroyAPIView(DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = (ChatPermissions, )

class ChatMessageCreateAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCreateSerializer

    def perform_create(self, serializer):
        return serializer.save(from_user = self.request.user)

class ChatMessageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageCreateSerializer