from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics,authentication
from django.contrib.auth import get_user_model 

import json
from rest_framework import views
# from .models1 import SignUp,User_Details

from .serializer import UserSeriazlier,SignupSeriazlier,UserdetailSeriazlier
# from . import serializer
from django.contrib.auth import login
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.shortcuts import get_object_or_404
import base64

User = get_user_model() 
class TokenView(generics.ListCreateAPIView):
  
   
    serializer_class=UserdetailSeriazlier
    authentication_classes=[authentication.SessionAuthentication,
                            TokenAuthentication]  #here token and username,password required.(authentication with token)
    permission_classes=[IsAuthenticated] # need permission to access USER MODEL database
    
    # def perform_create(self, serializer):
    #     print(serializer.validated_data)
    #     title=serializer.validated_data.get('title')
    #     content= serializer.validated_data.get('title')
    #     serializer.save() 
    def get_queryset(self):
        user_name=self.request.user
        
        try:
            # user_name=SignUp.objects.get(user=user_name)
            print(user_name)
            user_obj= User.objects.filter(username=user_name) #This will filter user database as we required and it will display the Details of the Users from the django server

          
            return user_obj
        except Exception as e:
            print(e)


class SignUpView(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes=(AllowAny,) # allow anyone able to singup
    serializer_class=UserSeriazlier # this will create username and password
    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)
    #     return Response({
    #         'status': 201,
    #         'message': 'Testimonials fetched',
    #         'data': response.data
    #     })

    # def perform_create(self, serializer):
    #     print(serializer)
    #     serializer.save(owner=self.request.user)
#     #    print(serializer.validated_data)
#        username=serializer.validated_data.get('username')
#        password=serializer.validat3ed_data.get('password')
#        serializer.save()   

# class UserUpdateAPIview(generics.UpdateAPIView):
#     # queryset= User_Details.objects.all()
#     serializer_class=UserdetailSeriazlier
#     authentication_classes=[authentication.SessionAuthentication,TokenAuthentication]
#     permission_classes=[IsAuthenticated]
#     lookup_field = 'pk'


#     def update(self, request, args, *kwargs):
#         partial = kwargs.pop('partial', False)
#         print("--------------",partial)

#         instance = self.get_object()
        
        
#         print(instance) 
        
        
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         # print(serializer)

#         print(self)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         serializer.save()     
      
      
     
        
        
        
        
        
        
