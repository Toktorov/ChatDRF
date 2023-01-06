from django.urls import path
from apps.users.views import UserAPIViewSet, UserRegisterAPIView, UserRetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', UserAPIViewSet, basename='users')

urlpatterns = [
    path('current-user/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name = "api_users_update_delete"),
    #auth
    path('register/', UserRegisterAPIView.as_view(), name = "api_users_register"),
    path('login/', TokenObtainPairView.as_view(), name='api_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='api_token_refresh'),
]

urlpatterns += router.urls