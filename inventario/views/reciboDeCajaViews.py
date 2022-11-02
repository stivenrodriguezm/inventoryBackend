from rest_framework                                  import views
from rest_framework.response                         import Response
from rest_framework.decorators                       import api_view

from inventario.models import ReciboDeCaja, Caja, ValorEnCaja, Ventas
from django.db import connection


@api_view(['GET'])
def VerRecibosCaja(request):
    reciboDeCaja = ReciboDeCaja.objects.all()
    return Response(reciboDeCaja.values())

@api_view(['POST'])
def CrearReciboCaja(request):
    data = request.data
    metodo_pago = data['metodo_pago']
    id_venta = Ventas.objects.only("id_auto").get(id_auto = data["id_venta"])

    reciboCaja = ReciboDeCaja.objects.create(
        numero_recibo_caja = data['numero_recibo_caja'],
        id_venta = id_venta,
        metodo_pago = data['metodo_pago'],
        abono_cancelacion = data['abono_cancelacion'],
        fecha = data['fecha'],
        valor = data['valor'],
    )
    valor_rc = reciboCaja.valor
    venta = reciboCaja.id_venta
    id_auto = reciboCaja.id_auto
    numero_recibo_caja = reciboCaja.numero_recibo_caja

    if metodo_pago == "Efectivo":
        caja = Caja.objects.create(
            fecha = data['fecha'],
            concepto = str(numero_recibo_caja),
            tipo = 'Ingreso',
            subtipo = 'Ingresos con RC.',
            valor = data['valor'],
        )
        id_movimiento = caja.id_movimiento
        tipo = caja.tipo
        valor = caja.valor
        caja.save()

        valorCajaData = ValorEnCaja.objects.get(id = 1)
        valorCaja = valorCajaData.valorActual
        
        if tipo == "Ingreso":
            valorCaja = valorCaja + valor
        if tipo == "Egreso":
            valorCaja = valorCaja - valor
        if tipo == "Cierre":
            valorCaja = valorCaja

        valorCajaData.valorActual = valorCaja
        valorCajaData.save()

        caja = Caja.objects.get(id_movimiento = id_movimiento)
        caja.valorCaja = valorCaja
        caja.save()

    id_caja = Caja.objects.only("id_movimiento").get(id_movimiento = id_movimiento)

    reciboCaja.id_movimiento_caja = id_caja
    reciboCaja.save()

    venta = Ventas.objects.get(id_auto = data["id_venta"])
    abono = venta.abono + valor_rc
    venta.abono = abono
    venta.saldo = venta.valor_venta - abono
    venta.save()

    rcaja = ReciboDeCaja.objects.filter(id_auto = id_auto)

    return Response(rcaja.values())

@api_view(['DELETE'])
def EliminarReciboCaja(request, **kwargs):
    id_auto = kwargs['pk']
    data = request.data
    valor = data['valor']

    # Restar valor en caja
    valorCajaData = ValorEnCaja.objects.get(id = 1)
    valorCaja = valorCajaData.valorActual

    if data['metodo_pago'] == 'Efectivo': 
        valorCaja = valorCaja - valor

    valorCajaData.valorActual = valorCaja
    valorCajaData.save()

    # Eliminar entrada de caja
    caja = Caja.objects.get(id_movimiento = data['id_movimiento_caja_id'])
    caja.delete()

    # El recibo de caja se elimina gracias al modelo cascada al eliminar la entrada de caja

    return Response({'Eliminado correctamente'})

