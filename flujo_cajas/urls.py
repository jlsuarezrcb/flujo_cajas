"""flujo_cajas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from flujo_cajas.settings import MEDIA_ROOT,STATIC_ROOT,STATIC_URL,MEDIA_URL
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flujo/', include('apps.flujo.urls')),
    path('accounts/',include('registration.backends.default.urls')),
]+static(STATIC_URL,document_root=STATIC_ROOT)

urlpatterns+=static(MEDIA_URL,document_root=MEDIA_ROOT)
