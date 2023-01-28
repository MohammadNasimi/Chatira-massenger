from rest_framework import serializers
from accounts.models import User,profile
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'phone', 'password','email', 'first_name', 'last_name')
        read_only_fields = ('id','email', 'first_name', 'last_name')
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = ('id', 'user', 'username','bio', 'profile_pic')
        read_only_fields = ('id','user')
        