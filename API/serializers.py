from .models import *
from rest_framework import serializers

class ContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacto
        fields = ['nombre','apellido','direccion'] # "__all__"