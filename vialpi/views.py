from django.shortcuts import render
from rest_framework import generics,permissions
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from vialpi.serializers import RegisterSerializer, ContactUsSerializer
# Create your views here.

class SignUpApiView(generics.GenericAPIView):
    serializer_class=RegisterSerializer

    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({'user':RegisterSerializer(user,context=self.get_serializer_context()).data,})


class ContactApi(generics.GenericAPIView):
    serializer_class=ContactUsSerializer

    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        contact=serializer.save()
        return Response({'contact':ContactUsSerializer(contact,context=self.get_serializer_context()).data,})