from inventario.models.inventarioModels import Proveedores
from rest_framework import serializers

class VerProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedores
        fields = ['id_proveedor','nombre_proveedor','telefono_proveedor','direccion_proveedor']