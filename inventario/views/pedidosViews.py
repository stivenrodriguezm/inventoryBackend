from rest_framework                                  import views
from rest_framework.response                         import Response
from rest_framework.decorators                       import api_view

from inventario.models import Pedidos, Ventas, Proveedores, Vendedores

@api_view(['GET'])
def VerPedidos(request):
    pedidos    = Pedidos.objects.all()
    return Response(pedidos.values())

@api_view(['POST'])
def CrearPedido(request, *args, **kwargs):
    data = request.data
    venta = Ventas.objects.only("id_venta").get(id_auto = data['id_venta'])
    proveedor = Proveedores.objects.only("id_proveedor").get(id_proveedor = data['id_proveedor'])
    vendedor = Vendedores.objects.only("id_vendedor").get(id_vendedor = data['id_vendedor'])
    pedido = Pedidos.objects.create(
        id_orden_pedido = data['id_orden_pedido'],
        id_venta = venta,
        id_proveedor = proveedor,
        id_vendedor = vendedor,
        tela = data['tela'],
        fecha = data['fecha'],
        fecha_despacho = data['fecha_despacho'],
        enviada = data['enviada'],
        recibida = data['recibida'],
        valor_total = data['valor_total']
    )
    id_auto = pedido.id_auto
    pedido.save()
    pedido = Pedidos.objects.filter(id_auto = id_auto)
    return Response(pedido.values())

@api_view(['PUT'])
def EditarPedido(request, **kwargs):
    id_auto = kwargs['pk']
    data = request.data

    venta = Ventas.objects.only("id_venta").get(id_auto = data['id_venta'])
    proveedor = Proveedores.objects.only("id_proveedor").get(id_proveedor = data['id_proveedor'])
    vendedor = Vendedores.objects.only("id_vendedor").get(id_vendedor = data['id_vendedor'])

    pedido = Pedidos.objects.get(id_auto = id_auto)
    pedido.id_orden_pedido = data['id_orden_pedido']
    pedido.id_venta = venta
    pedido.id_proveedor = proveedor
    pedido.id_vendedor = vendedor
    pedido.tela = data['tela']
    pedido.fecha = data['fecha']
    pedido.fecha_despacho = data['fecha_despacho']
    pedido.enviada = data['enviada']
    pedido.recibida = data['recibida']
    pedido.valor_total = data['valor_total']
    pedido.save()

    pedido = Pedidos.objects.filter(id_auto = id_auto)
    return Response(pedido.values())

@api_view(['DELETE'])
def EliminarPedido(request, **kwargs):
    id_auto = kwargs['pk']
    pedido = Pedidos.objects.get(id_auto = id_auto)
    pedido.delete()
    return Response({"El pedido fue eliminado"})