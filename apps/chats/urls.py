from django.urls import path
from apps.chats.views import ChatAPIView, ChatRetrieveAPIView, ChatMessageCreateAPIView, ChatDestroyAPIView, ChatMessageRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('', ChatAPIView.as_view(), name = 'api_chats'),
    path('chat/<int:pk>/', ChatRetrieveAPIView.as_view(), name = 'api_detail_chat'),
    path('chat/destroy/<int:pk>', ChatDestroyAPIView.as_view(), name = "api_destroy_chat"),
    path('message/create/', ChatMessageCreateAPIView.as_view(), name = 'api_message_create'),
    path('message/<int:pk>/', ChatMessageRetrieveUpdateDestroyAPIView.as_view(), name = 'api_message_update_destroy'),
]