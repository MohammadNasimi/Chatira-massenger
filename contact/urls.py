from django.urls import path 
from contact.views import  *
urlpatterns = [
    path('create/', CreateContactView.as_view(), name='create_contact'),
    path('filter/', FilterContactView.as_view(), name='filter_contact'),
    path('update/<int:pk>/',UpdateContactView.as_view(), name='update_contact'),
]
