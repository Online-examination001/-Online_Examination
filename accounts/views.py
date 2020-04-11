from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import RegistrationSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth import login, logout
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated





class RegisterView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs ):

        if request.method == "GET":
            return Response({"message":"Get method not allowed"})
        serializer = RegistrationSerializer(data = request.data)

        data = {}

        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "succesfully registered"
            data['email'] = user.email
            data['username'] = user.username
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors

        return Response({"data":data})





class LogoutView(APIView):
    authentication_classes = [IsAuthenticated, ]
    permission_classes = [AllowAny]

    def get(self,request):
        logout(request)
        return Response({
            "message": "Logged out succesfully"
        }, status = 200)

 
