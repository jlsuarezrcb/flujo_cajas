from django.urls import path

from apps.flujo import views

urlpatterns = [
    path('home/', views.Home.as_view(), name='view_home'),
    # activos
    path('activo/listar', views.ActivoView.as_view(), name='view_activo_listar'),
    path('activo/editar/<int:pk>/', views.ActivoUpdateView.as_view(), name='view_activo_update'),
    path('activo/crear', views.ActivoCreate.as_view(), name='view_activo_crear'),
    path('activo/eliminar/<int:pk>/', views.ActivoDelete.as_view(), name='view_activo_eliminar'),
    # acredor
    path('acredor/listar', views.AcredorView.as_view(), name='view_acredor_listar'),
    path('acredor/editar/<int:pk>/', views.AcredorUpdateView.as_view(), name='view_acredor_update'),
    path('acredor/crear', views.AcredorCreate.as_view(), name='view_acredor_crear'),
    path('contacto/', views.Contacto.as_view(), name='view_contacto'),

]
