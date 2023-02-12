#rest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions,filters,generics

#serializers
from contact.serialiazer import ContactSerializer
#models
from contact.models import contact
from accounts.models import profile
from contact.permissions import update_contact_permissions
# drf-ysg for swagger import
from drf_yasg.utils import swagger_auto_schema
from contact import docs

class CreateContactView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    @swagger_auto_schema(operation_description=docs.contact_create_post,tags=['contacts'])
    def post(self, request, *args, **kwargs):
        name = request.data.get("name" ,"")
        if request.data.get('phone') == None:
            return Response({"detail": "please fill phone "} , status=status.HTTP_400_BAD_REQUEST)
        
        profile_user = profile.objects.get(user_id = self.request.user.id)
        try:
            profile_contact = profile.objects.get(user__phone = request.data.get('phone'))

        except:
            return Response({"detail"  : "phone does not exist"} , status=status.HTTP_400_BAD_REQUEST)
        try:
            contact.objects.get(user_id = profile_user.id,contact_id=profile_contact.id)
            return Response({"detail"  : "phone exist in your contact list"}, status=status.HTTP_201_CREATED)
        except:
            contact.objects.create(user_id = profile_user.id,name_contract= name
                                    ,contact_id=profile_contact.id)

        return Response(request.data, status=status.HTTP_201_CREATED)

class FilterContactView(generics.ListAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_contact','contact__user__phone']


    def get_queryset(self):
        search_query = self.request.GET.get('search',None)
        profile_user = profile.objects.get(user_id = self.request.user.id)
        queryset = contact.objects.filter(user_id= profile_user.id) 
        if search_query :
            queryset = queryset.filter(name_contact__icontains=search_query)
            queryset = queryset.filter(contact__user__phone__icontains=search_query)
        return queryset
    @swagger_auto_schema(operation_description=docs.contact_create_post,tags=['contacts'])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class UpdateContactView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated,update_contact_permissions]
    queryset = contact.objects.all()
    @swagger_auto_schema(operation_description=docs.contact_detail_get,tags=['contacts'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.contact_detail_put,tags=['contacts'])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.contact_detail_patch,tags=['contacts'])
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.contact_detail_delete,tags=['contacts'])
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)