from rest_framework import serializers
from contact.models import contact
class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = contact
        fields = ('user','contact','block')
        only_read_field = ('user')
