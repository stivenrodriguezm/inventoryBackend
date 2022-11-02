from django.urls import path
from .views import (proveedoresViews, 
                    productosViews, 
                    categoriasViews, 
                    facturasViews, 
                    remisionesViews, 
                    ventasViews, 
                    vendedoresViews, 
                    transportadoresViews,
                    ordenPedidoViews,
                    entregadosStock,
                    pedidosViews,
                    cajaViews,
                    comprobantesDeEgresoViews,
                    reciboDeCajaViews
                    )

urlpatterns = [
    path('proveedores/', proveedoresViews.VerProveedores, name="verProveedores"),
    path('nuevoProveedor/', proveedoresViews.CrearProveedores, name="crearProveedor"),
    path('editarProveedor/<str:pk>', proveedoresViews.EditarProveedor, name="editarProveedor"),
    path('eliminarProveedor/<str:pk>', proveedoresViews.EliminarProveedor, name="eliminarProveedor"),
 
    path('productos/', productosViews.VerProductos, name="verProductos"),
    path('products/<categoria>', productosViews.ProductosPorCategoria, name="ProductosPorCategoria"),
    path('nuevoProducto/', productosViews.CrearProducto, name="CrearProducto"),
    path('editarProducto/<str:pk>', productosViews.EditarProducto, name="editarProducto"),
    path('eliminarProducto/<str:pk>', productosViews.EliminarProducto, name="eliminarProducto"),

    path('categorias/', categoriasViews.VerCategorias, name="VerCategorias"),
    path('nuevaCategoria/', categoriasViews.CrearCategoria, name="CrearCategoria"),
    path('editarCategoria/<str:pk>', categoriasViews.EditarCategoria, name="EditarCategoria"),
    path('eliminarCategoria/<str:pk>', categoriasViews.EliminarCategoria, name="EliminarCategoria"),

    path('facturas/', facturasViews.VerFacturas, name="VerFacturas"),
    path('nuevaFactura/', facturasViews.CrearFactura, name="CrearFactura"),
    path('editarFactura/<str:pk>', facturasViews.EditarFactura, name="EditarFactura"),
    path('eliminarFactura/<str:pk>', facturasViews.EliminarFactura, name="EliminarFactura"),
    
    path('stock/', facturasViews.VerStock, name="VerStock"),
    path('nuevoStock/', facturasViews.CrearStock, name="nuevoStock"),
    path('editarStock/<str:pk>', facturasViews.EditarStock, name="EditarStock"),
    path('eliminarStock/<str:pk>', facturasViews.EliminarStock, name="EliminarStock"),
    
    path('entregadosStock/', entregadosStock.VerEntregadosStock, name="VerEntregadosStock"),

    path('remisiones/', remisionesViews.VerRemisiones, name="VerRemisiones"),
    path('nuevaRemision/', remisionesViews.CrearRemision, name="CrearRemision"),
    path('editarRemision/<str:pk>', remisionesViews.EditarRemision, name="EditarRemision"),
    path('eliminarRemision/<str:pk>', remisionesViews.EliminarRemision, name="EliminarRemision"),

    path('pedidos/', pedidosViews.VerPedidos, name="VerPedidos"),
    path('nuevoPedido/', pedidosViews.CrearPedido, name="CrearPedido"),
    path('editarPedido/<str:pk>', pedidosViews.EditarPedido, name="EditarPedido"),
    path('eliminarPedido/<str:pk>', pedidosViews.EliminarPedido, name="EliminarPedido"),

    path('ventas/', ventasViews.VerVentas, name="Ver Ventas"),
    path('nuevaVenta/', ventasViews.CrearVenta, name="CrearVenta"),
    path('editarVenta/<str:pk>', ventasViews.EditarVenta, name="EditarVenta"),
    path('eliminarVenta/<str:pk>', ventasViews.EliminarVenta, name="EliminarVenta"),

    path('vendedores/', vendedoresViews.VerVendedores, name="VerVendedores"),
    path('nuevoVendedor/', vendedoresViews.CrearVendedor, name="CrearVendedores"),
    path('editarVendedor/<str:pk>', vendedoresViews.EditarVendedor, name="EditarVendedores"),
    path('eliminarVendedor/<str:pk>', vendedoresViews.EliminarVendedor, name="EliminarVendedores"),

    path('transportadores/', transportadoresViews.VerTransportadores, name="Vertransportadores"),
    path('nuevoTransportador/', transportadoresViews.CrearTransportador, name="Creartransportador"),
    path('editarTransportador/<str:pk>', transportadoresViews.EditarTransportador, name="Editartransportador"),
    path('eliminarTransportador/<str:pk>', transportadoresViews.EliminarTransportador, name="Eliminartransportador"),

    path('ordenesPedido/', ordenPedidoViews.VerOrdenesPedido, name="VerOrdenPedido"),
    path('nuevaOrdenPedido/', ordenPedidoViews.CrearOrdenPedido, name="CrearOrdenPedido"),
    path('editarOrdenPedido/<str:pk>', ordenPedidoViews.EditarOrdenPedido, name="EditarOrdenPedido"),
    path('eliminarOrdenPedido/<str:pk>', ordenPedidoViews.EliminarOrdenPedido, name="EliminarOrdenPedido"),

    path('caja/', cajaViews.VerCaja, name="VerCaja"),
    path('saldoActualCaja/', cajaViews.SaldoActualCaja, name="SaldoActualCaja"),
    path('crearCaja/', cajaViews.CrearCaja, name="CrearCaja"),
    # path('editarOrdenPedido/<str:pk>', ordenPedidoViews.EditarOrdenPedido, name="EditarOrdenPedido"),
    path('eliminarCaja/<str:pk>', cajaViews.EliminarCaja , name="EliminarCaja"),

    path('reciboDeCaja/', reciboDeCajaViews.VerRecibosCaja , name="VerRecibosCaja"),
    path('crearReciboCaja/', reciboDeCajaViews.CrearReciboCaja, name="CrearReciboCaja"),
    path('eliminarReciboCaja/<str:pk>', reciboDeCajaViews.EliminarReciboCaja , name="EliminarReciboCaja"),

    path('comprobantesDeEgreso/', comprobantesDeEgresoViews.VerCEs , name="comprobantesDeEgreso"),
    path('crearComprobanteDeEgreso/', comprobantesDeEgresoViews.CrearCE, name="CrearComprobanteDeEgreso"),
    path('eliminarComprobanteDeEgreso/<str:pk>', comprobantesDeEgresoViews.EliminarCE , name="eliminarComprobanteDeEgreso"),

]