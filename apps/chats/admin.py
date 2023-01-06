from django.contrib import admin
from apps.chats.models import Chat, Message

# Register your models here.
class ChatAdmin(admin.ModelAdmin):
    list_filter = ('id', )
    list_display = ('from_chat_user', 'to_chat_user', 'created_at')
    search_fields = ('from_chat_user', 'to_chat_user', 'created_at')
    list_per_page = 20

class MessageAdmin(admin.ModelAdmin):
    list_filter = ('id', )
    list_display = ('chat', 'from_user', 'to_user', 'is_read', 'created_at')
    search_fields = ('chat', 'from_user', 'to_user', 'is_read', 'created_at')
    list_per_page = 20

admin.site.register(Chat, ChatAdmin)
admin.site.register(Message, MessageAdmin)