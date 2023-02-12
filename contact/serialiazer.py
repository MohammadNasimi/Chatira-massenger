from rest_framework import serializers
from contact.models import contact
from accounts.serializer import ProfileSerializer
class ContactSerializer(serializers.ModelSerializer):
    user =  ProfileSerializer( read_only=True)
    contact =  ProfileSerializer(read_only=True)

    class Meta:
        model = contact
        fields = ('user','name_contract','contact','block')
        only_read_field = ('user')
