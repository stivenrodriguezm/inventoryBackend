from rest_framework                                  import views
from rest_framework.response                         import Response
from rest_framework.decorators                       import api_view

from inventario.models import Caja, ValorEnCaja
from django.db import connection


@api_view(['GET'])
def VerCaja(request):
    caja = Caja.objects.all()
    return Response(caja.values())

@api_view(['GET'])
def SaldoActualCaja(request):
    caja = ValorEnCaja.objects.all()
    return Response(caja.values())

@api_view(['POST'])
def CrearCaja(request):
    data = request.data
    
    caja = Caja.objects.create(
        fecha = data['fecha'],
        concepto = data['concepto'],
        tipo = data['tipo'],
        subtipo = data['subtipo'],
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

    caja = Caja.objects.filter(id_movimiento = id_movimiento)

    return Response(caja.values())


@api_view(['DELETE'])
def EliminarCaja(request, **kwargs):
    id_movimiento = kwargs['pk']
    caja = Caja.objects.get(id_movimiento = id_movimiento)
    tipo = caja.tipo
    valor = caja.valor
    
    valorCajaData = ValorEnCaja.objects.get(id = 1)
    valorCaja = valorCajaData.valorActual

    if tipo == "Ingreso":
        valorCaja = valorCaja - valor
    if tipo == "Egreso":
        valorCaja = valorCaja + valor
    if tipo == "Cierre":
        valorCaja = valorCaja
    else:
        valorCaja = valorCaja - valor

    valorCajaData.valorActual = valorCaja
    valorCajaData.save()
    
    caja.delete()

    return Response({f'Éxito, el nuevo saldo en caja es: ${valorCaja}'})