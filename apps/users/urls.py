from django.urls import path
from apps.users.views import UsersAPIView


urlpatterns = [
    path('api/users/', UsersAPIView.as_view(), name='api_users'),
]