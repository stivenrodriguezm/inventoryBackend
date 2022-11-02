from django.urls import path, include

urlpatterns = [
    path('inventario/', include('inventario.urls'))
]
