from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth import get_user_model
from core.serializer import MyTokenObtainPair,UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class MyCreateView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

MyCreateViewClass = MyCreateView.as_view()
class MyTokenView(TokenObtainPairView):
    serializer_class = MyTokenObtainPair

myTokenViewClass = MyTokenView.as_view()