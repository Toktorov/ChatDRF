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

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('message', 'chat')

    def validate(self, attrs):
        try:
            chat = Chat.objects.get(pk = self.initial_data['chat'], from_chat_user = self.context['request'].user)
        except:
            chat = Chat.objects.get(pk = self.initial_data['chat'], to_chat_user = self.context['request'].user)
        return attrs

    def create(self, validated_data):
        chat = Chat.objects.get(pk = self.initial_data['chat'])
        message = Message.objects.create(chat = validated_data['chat'], message = validated_data['message'], from_user = self.context['request'].user, to_user = chat.to_chat_user)
        message.save()
        return message

class MessageUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('message', 'chat')

    def validate(self, attrs):
        try:
            chat = Chat.objects.get(pk = self.initial_data['chat'], from_chat_user = self.context['request'].user)
        except:
            chat = Chat.objects.get(pk = self.initial_data['chat'], to_chat_user = self.context['request'].user)
        return attrs

    def update(self, validated_data):
        chat = Chat.objects.get(pk = self.initial_data['chat'])
        message = Message.objects.get(pk = chat.id)
        message.message = validated_data['message']
        message.save()
        return message

class ChatChatRetrieveSerializer(serializers.ModelSerializer):
    messages_chat = MessageSerializer(read_only = True, many = True)

    class Meta:
        model = Chat
        fields = ('id', 'from_chat_user', 'to_chat_user', 'messages_chat')