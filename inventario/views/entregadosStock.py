from rest_framework                                  import views
from rest_framework.response                         import Response
from rest_framework.decorators                       import api_view

from inventario.models import EntregadosStock

@api_view(['GET'])
def VerEntregadosStock(request):
    entregadosStock    = EntregadosStock.objects.all()
    return Response(entregadosStock.values())

@api_view(['POST'])
def CrearStock(request, *args, **kwargs):
    data = request.data
    print(data)
    stock = EntregadosStock.objects.create(
        id_factura = data['id_factura'],
        id_producto = data['id_producto'],
        id_proveedor = data['id_proveedor'],
        valor = data['valor'],
        disponible = data['disponible'],
        nota = data['nota']
    )
    stock.save()
    return Response({'stock creado'})