from django.urls import path 
from rest_framework_simplejwt import views as jwt_views
from accounts.views import  LoginView,RegisterView,ProfileView,UserMetaView
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', jwt_views.TokenRefreshView.as_view(), name='login_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/detail/<int:pk>/', ProfileView.as_view(), name='profile_detail'),
    path('user_meta/detail/<int:pk>/', UserMetaView.as_view(), name='user_meta_detail'),


]