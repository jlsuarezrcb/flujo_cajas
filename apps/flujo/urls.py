from django.urls import path


from apps.flujo import views

urlpatterns = [
    path('home/', views.Home.as_view(), name='view_home'),
    path('activo/listar', views.ActivoView.as_view(), name='view_activo_listar'),
    path('activo/crear', views.ActivoCreate.as_view(), name='view_activo_crear'),
    path('contacto/', views.Contacto.as_view(), name='view_contacto'),

]

