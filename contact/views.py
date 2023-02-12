#rest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
#serializers
from contact.serialiazer import ContactSerializer
#models
from contact.models import contact
from accounts.models import profile


class CreateContactView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        if request.data.get('phone') == None:
            return Response({"detail": "please fill phone "} , status=status.HTTP_400_BAD_REQUEST)
        
        profile_user = profile.objects.get(user_id = self.request.user.id)
        try:
            profile_contact = profile.objects.get(user__phone = request.data.get('phone'))

        except:
            return Response({"detail"  : "phone does not exist"} , status=status.HTTP_400_BAD_REQUEST)
        
        contact.objects.create(user_id = profile_user.id,contact_id=profile_contact)

        return Response(request.data, status=status.HTTP_201_CREATED)
