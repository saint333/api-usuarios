from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('id','nombre','apellido','usuario','correo','contraseña','telefono','sexo','cumpleaño','dia_registro')
        read_only_fields = ('dia_registro',)