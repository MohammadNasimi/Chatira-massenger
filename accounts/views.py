#rest 
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# jwt
from rest_framework_simplejwt.tokens import RefreshToken
#account 
from accounts.models import User,profile,user_meta
from accounts.permissions import * 
#serializer
from accounts.serializer import *
#django auth 
from django.contrib.auth import authenticate
# drf-ysg for swagger import
from drf_yasg.utils import swagger_auto_schema
from accounts import docs
# log in
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    @swagger_auto_schema(operation_description=docs.Log_in_Post,tags=['accounts'])
    def post(self, request, *args, **kwargs):
        if "password" not in request.data or "phone" not in request.data:
            return Response({"detail": "please send phone and password"} , status=status.HTTP_400_BAD_REQUEST)
        def get_token(user):
                refresh = RefreshToken.for_user(user)
                return {
                    'refresh':str(refresh),
                    'access':str(refresh.access_token)
                }

        user = authenticate(phone = request.data['phone'],password = request.data['password'])
        if user :
            data = LoginSerializer(user).data
            token=get_token(user)
            data['refresh']=token['refresh']
            data['access']=token['access']
            profile_id =profile.objects.get(user_id = user.id).id
            data['profile_id'] = profile_id
            data['user_meta_id'] = user_meta.objects.get(profile_id = profile_id).id

            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response({'user':'wrong username or password'}, status=status.HTTP_200_OK)

# register
class RegisterView(APIView):
    @swagger_auto_schema(operation_description=docs.Register_create_Post,tags=['accounts'])
    def post(self, request, *args, **kwargs):
        email= request.data.get("email" ,"")
        first_name= request.data.get("first_name" ,"")
        last_name= request.data.get("last_name" ,"")
        # create-user
        def create_users():
            user =User.objects.create_user(phone=request.data.get('phone'),password=request.data.get('password'),
                email=email,first_name=first_name,last_name=last_name)
            return user
        if request.data.get('phone') == None or request.data.get('password') == None :
            return Response({"detail": "please fill phone password"} , status=status.HTTP_400_BAD_REQUEST)
        try:
            user_create = create_users()
            profile_create = profile.objects.create(user =user_create)   
            user_meta.objects.create(profile = profile_create)
        except:
            return Response({"detail"  : "phone exist"} , status=status.HTTP_400_BAD_REQUEST)
        
        return Response(request.data, status=status.HTTP_201_CREATED)
    
# profile detail and update 
class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes =[IsAuthenticated,profile_permissions]
    serializer_class = ProfileSerializer
    queryset = profile.objects.all()
    @swagger_auto_schema(operation_description=docs.profile_detail_Get,tags=['accounts'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.profile_detail_put,tags=['accounts'])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.profile_detail_patch,tags=['accounts'])
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class UserMetaView(generics.RetrieveUpdateAPIView):
    permission_classes =[IsAuthenticated,user_meta_permissions]
    serializer_class = UserMetaSerializer
    queryset = user_meta.objects.all()
    @swagger_auto_schema(operation_description=docs.usermeta_detail_Get,tags=['accounts'])
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.usermeta_detail_put,tags=['accounts'])
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    @swagger_auto_schema(operation_description=docs.usermeta_detail_patch,tags=['accounts'])
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
