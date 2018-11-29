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
    path('acredor/eliminar/<int:pk>/', views.AcredorDelete.as_view(), name='view_acredor_eliminar'),
    # categoria
    path('categoria/listar', views.CategoriaView.as_view(), name='view_categoria_listar'),
    path('categoria/editar/<int:pk>/', views.CategoriaUpdateView.as_view(), name='view_categoria_update'),
    path('categoria/crear', views.CategoriaCreateView.as_view(), name='view_categoria_crear'),
    path('categoria/eliminar/<int:pk>/', views.CategoriaDelete.as_view(), name='view_categoria_eliminar'),
    # subcategoria
    path('subcategoria/listar', views.SubCategoriaView.as_view(), name='view_subcategoria_listar'),
    path('subcategoria/editar/<int:pk>/', views.SubCategoriaUpdateView.as_view(), name='view_subcategoria_update'),
    path('subcategoria/crear', views.SubCategoriaCreateView.as_view(), name='view_subcategoria_crear'),
    path('subcategoria/eliminar/<int:pk>/', views.SubCategoriaDelete.as_view(), name='view_subcategoria_eliminar'),
    # obligaciones
    path('obligaciones/listar', views.ObligacionesView.as_view(), name='view_obligaciones_listar'),
    path('obligaciones/editar/<int:pk>/', views.ObligacionesUpdateView.as_view(), name='view_obligacion_update'),
    path('obligaciones/crear', views.ObligacionesCreateView.as_view(), name='view_obligacion_crear'),
    path('obligaciones/eliminar/<int:pk>/', views.ObligacionesDelete.as_view(), name='view_obligacion_eliminar'),
    # otro
    # path('contacto/', views.Contacto.as_view(), name='view_contacto'),

]
