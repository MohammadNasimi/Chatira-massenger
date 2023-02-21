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
#OTP
from accounts.helper import *
# log in
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    @swagger_auto_schema(operation_description=docs.Log_in_Post,tags=['accounts'])
    def post(self, request, *args, **kwargs):
        if "phone" not in request.data or "otp" not in request.data:
            return Response({"detail": "please send phone and otp"} , status=status.HTTP_400_BAD_REQUEST)
        def get_token(user):
                refresh = RefreshToken.for_user(user)
                return {
                    'refresh':str(refresh),
                    'access':str(refresh.access_token)
                }
        user_get = User.objects.get(phone = request.data['phone'])
        #check otp expire time
        if not check_otp_expiration(request.data['phone']):
            return Response({'user':'otp expire time finish '}, status=status.HTTP_200_OK)

        if user_get.otp != int(request.data['otp']):
            return Response({'user':'wrong otp '}, status=status.HTTP_200_OK)
        
        user = authenticate(phone = request.data['phone'])
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
            return Response({'user':'wrong phone '}, status=status.HTTP_200_OK)

# register
class RegisterView(APIView):
    @swagger_auto_schema(operation_description=docs.Register_create_Post,tags=['accounts'])
    def post(self, request, *args, **kwargs):
        email= request.data.get("email" ,"")
        first_name= request.data.get("first_name" ,"")
        last_name= request.data.get("last_name" ,"")
        # create-user
        def create_users():
            user =User.objects.create_user(phone=request.data.get('phone'),
                email=email,first_name=first_name,last_name=last_name)
            return user
        if request.data.get('phone') == None  :
            return Response({"detail": "please fill phone "} , status=status.HTTP_400_BAD_REQUEST)
        #send_otp
        otp = get_random_otp()
        print(otp)
        # send_otp(request.data.get('phone'),otp)
        
        try:
            user_create = create_users()
            #save otp
            user_create.otp = otp
            user_create.save()
            profile_create = profile.objects.create(user =user_create)   
            user_meta.objects.create(profile = profile_create)
        except:
            user =User.objects.get(phone = request.data.get('phone'))
            #save otp
            user.otp = otp
            user.otp_create_time = datetime.now(timezone.utc)
            user.save()
            # return Response({"detail"  : "phone exist"} , status=status.HTTP_400_BAD_REQUEST)
        
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
