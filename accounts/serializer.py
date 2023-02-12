from rest_framework import serializers
from accounts.models import User,profile,user_meta
class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'phone', 'password','email', 'first_name', 'last_name')
        read_only_fields = ('id','email', 'first_name', 'last_name')
        
class ProfileSerializer(serializers.ModelSerializer):
    user = LoginSerializer(read_only=True)
    class Meta:
        model = profile
        fields = ('id', 'user', 'username','bio', 'profile_pic')
        read_only_fields = ('id','user')

class UserMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_meta
        fields = ('id', 'profile', 'personal_theme','status', 'last_seen')
        read_only_fields = ('id','profile')
        