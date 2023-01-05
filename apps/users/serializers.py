from rest_framework import serializers
from apps.users.models import User 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'phone_number','age', 'profile_image', 'bio')