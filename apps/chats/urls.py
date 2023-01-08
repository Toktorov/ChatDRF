from django.urls import path
from apps.chats.views import ChatAPIView, ChatRetrieveAPIView


urlpatterns = [
    path('', ChatAPIView.as_view(), name = 'api_chats'),
    path('chat/<int:pk>/', ChatRetrieveAPIView.as_view(), name = 'api_detail_chat')
]