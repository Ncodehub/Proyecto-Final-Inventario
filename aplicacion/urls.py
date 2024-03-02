from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('conoceme/', conoceme, name="conoceme"),
    ##______________________Repuestos________________________________________________
    path('repuestos/',RepuestosList.as_view(), name="repuestos"),
    path('repuestos_create/',RepuestoCreate.as_view() , name="repuestos_create"),
    path('repuestos_update/<int:pk>/',RepuestoUpdate.as_view() , name="repuestos_update"),
    path('repuestos_delete/<int:pk>/',RepuestoDelete.as_view() , name="repuestos_delete"),
    ##______________________Maquina________________________________________________
    path('maquina/',MaquinaList.as_view(), name="maquina"),
    path('maquina_create/',MaquinaCreate.as_view() , name="maquina_create"),
    path('maquina_update/<int:pk>/',MaquinaUpdate.as_view() , name="maquina_update"),
    path('maquina_delete/<int:pk>/',MaquinaDelete.as_view() , name="maquina_delete"),
    ##______________________Proveedores________________________________________________
    path('proveedor/',ProveedorList.as_view(), name="proveedores"),
    path('proveedor_create/',ProveedorCreate.as_view() , name="proveedor_create"),
    path('proveedor_update/<int:pk>/',ProveedorUpdate.as_view() , name="proveedor_update"),
    path('proveedor_delete/<int:pk>/',ProveedorDelete.as_view() , name="proveedor_delete"),
    ##___________________________________________________________________________________
    path('buscar/', buscar, name="buscar"),
    path('buscarRepuestos/', buscarRepuestos, name="buscarRepuestos"),
    ##_____________________Solicitud de Repuesto_____________________________________
    path('solicitudrepuesto/',SolicitudRepuestoList.as_view(), name="solicitudrepuesto"),
    path('sol_repuesto_create/',SolicitudRepuestoCreate.as_view() , name="sol_repuesto_create"),

    #_______________________Login-Logout-Registro-EditarPerfil___________________________________
    path('login/',login_request, name="login"),
    path('registro/',register, name="registro"),
    path('logout/',LogoutView.as_view(template_name = "aplicacion/logout.html"), name="logout"),
    path('editar_perfil/',editarPerfil, name="editar_perfil"),
    path('agregar_avatar/',agregarAvatar, name="agregar_avatar"),
]