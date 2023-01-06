from django.urls import path
from apps.chats.views import ChatAPIView


urlpatterns = [
    path('', ChatAPIView.as_view(), name = 'api_chats'),
]