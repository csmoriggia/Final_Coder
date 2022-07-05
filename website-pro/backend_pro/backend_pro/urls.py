"""backend_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

from pro_website import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path("afiliate/", views.afiliate),
    path("contacto/", views.contacto),
    path("fiscalizacion/", views.fiscalizacion),
    path("", views.index),
    path("juventud/", views.carga_juventud),
    path("juventud/carga_juventud", views.carga_juventud),
    path("nuestros_proyectos/", views.nuestros_proyectos),
    path("quienes_somos/", views.quienes_somos),
    path("afiliate/afiliacion", views.afiliacion),
    path("fiscalizacion/fiscalizacion", views.fiscalizacion),
    path("buscar_afiliado", views.buscar_afiliado, name = 'Buscar_Afiliado'),
    path('busqueda_afiliado/', views.busqueda_afiliado),
    path('login/', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', LogoutView.as_view(template_name='index.html'), name = 'logout'),
    path('leer_afiliados/', views.leer_afiliados, name = "leer_afiliados"),
    path("eliminar_afiliado/<int:id>", views.eliminar_afiliado, name ="eliminar_afiliado"), 
    path("editar_afiliado/<int:id>", views.editar_afiliado, name ="editar_afiliado"), 
    path("editar_afiliado/", views.editar_afiliado, name ="editar_afiliado"), 
    path('editar_perfil/<int:id>', views.editar_perfil , name='editar_perfil'),
    path('agregar_proyecto', views.agregar_proyecto , name='agregar_proyecto'),
    path('eliminar_usuario/<int:id>', views.eliminar_usuario , name='eliminar_usuario'),
    path('leer_usuario/', views.leer_usuario, name = "leer_usuario"),
    path('nuestros_proyectos/proyecto/<int:id>', views.ver_proyecto, name="ver_proyecto"),
    path('leer_proyectos/', views.leer_proyectos, name = "leer_proyectos"),
    path('editar_proyecto/<int:id>', views.editar_proyecto, name="editar_proyecto"),
    path('eliminar_proyecto/<int:id>', views.eliminar_proyecto, name="eliminar_proyecto"),
]   

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)