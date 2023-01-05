from django.urls import path
from apps.users.views import UsersAPIView, UserRegisterAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('api/users/', UsersAPIView.as_view(), name='api_users'),
    #auth
    path('api/users/register/', UserRegisterAPIView.as_view(), name = "api_users_register"),
    path('api/users/login/', TokenObtainPairView.as_view(), name='api_login'),
    path('api/users/token/refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
]