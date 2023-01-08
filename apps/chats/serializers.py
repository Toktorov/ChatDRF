from rest_framework import serializers
from apps.chats.models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat 
        fields = "__all__"

    def validate(self, attrs):
        if attrs['from_chat_user'] == attrs['to_chat_user']:
            raise serializers.ValidationError({"error": "Нельзя писать самому себе"})
        if Chat.objects.filter(from_chat_user = attrs['from_chat_user'], to_chat_user = attrs['to_chat_user']).exists() or Chat.objects.filter(to_chat_user = attrs['from_chat_user'], from_chat_user = attrs['to_chat_user']).exists():
            raise serializers.ValidationError({"exits" : "Такой чат уже существует"})
        return attrs