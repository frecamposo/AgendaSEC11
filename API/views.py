from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
class ContactoViewSet(generics.ListCreateAPIView):
    queryset = Contacto.objects.all()
    serializer_class =  ContactoSerializer
