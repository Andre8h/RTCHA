from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView

# Create your views here.

@api_view(['GET','POST'])
def accounts(request):
    return Response("Accounts",status=status.HTTP_200_OK)

class login(APIView): #Login (View)controller
    def get(self,request):

        auth.post()
        return Response("Login",status=status.HTTP_200_OK)
    
    def post(self,request):
        return Response()

class auth(APIView): #Auth (View)controller
    def get(self,request):
        return Response("Auth",status=status.HTTP_200_OK)
    def post(self,request):
        
        return Response()
    
class signup(APIView): #Signup (View)controller
    def get(self,request):
        
        return Response("Signup",status=status.HTTP_200_OK)
    
    def post(self,request):
        return Response()

class profile(APIView): #Profile (View)controller
    def get(self,request,id):
        return Response({"Profile": "with id " + str(id)},status=status.HTTP_200_OK)
