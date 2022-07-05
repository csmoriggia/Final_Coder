from urllib import request
from django.db import reset_queries

from django.http import HttpResponse
from django.template import loader, context, Template
from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test


from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


from pro_website.models import *
from pro_website.forms import *


# Create your views here.


def afiliate(request):
    return render(request, "afiliate.html")

def contacto(request):
    return render(request, "contacto.html")

def index(request):
    avatares= Avatar.objects.filter(user=request.user.id)
    return render(request, 'index.html' , {"url":avatares[0].imagen.url})

def jpro(request):
    return render(request, "juventud.html")

def nuestros_proyectos(request,):

    proyectos = proyecto.objects.all()

    contexto = {"proyectos":proyectos}

    return render(request, "nuestros_proyectos.html", contexto)


def quienes_somos(request):
    return render(request, "quienes_somos.html")

def fiscalizacion(request):
    return render(request, "fiscalizacion.html")


def login_request(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)


            if user is not None:
                login(request, user)

                return render(request,"index.html", {"mensaje":f"Bienvenido {usuario}"} )

            else:

                return render(request,"index.html", {"mensaje":"Error, datos incorrectos"} )

        else:

                return render(request,"index.html", {"mensaje":"Error, formulario erróneo"} )

                
    form = AuthenticationForm()

    return render(request , "login.html" , {'form':form} )

def register(request):

    if request.method == 'POST':


        form = UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            return render (request, "index.html" , {"mensaje":"Usuario creado"})

    else:

        form = UserCreationForm()
    return render(request, "registro.html" , {"form":form})

def afiliacion(request):
    if request.method == "POST":
        afiliate = afiliado( nombre=request.POST['nombre'], apellido=request.POST['apellido'], direccion=request.POST['direccion'], dni=request.POST['dni'], fecha_nacimiento=request.POST['fecha_nacimiento'], telefono=request.POST['telefono'])
        afiliado.save(afiliate)
        return render(request, "afiliate.html")
    return render( request, "afiliate.html")    

def fiscalizacion(request):
    if request.method == "POST":
        fiscaliza = fiscal( nombre=request.POST['nombre'], apellido=request.POST['apellido'], direccion=request.POST['direccion'], dni=request.POST['dni'], fecha_nacimiento=request.POST['fecha_nacimiento'], telefono=request.POST['telefono'])
        fiscal.save(fiscaliza)
    return render( request, "fiscalizacion.html")

def carga_juventud(request):
    if request.method == "POST":
        joven = juventud( nombre=request.POST['nombre'], apellido=request.POST['apellido'], fecha_nacimiento=request.POST['fecha_nacimiento'], telefono=request.POST['telefono'], redes_sociales=request.POST['redes_sociales'])
        juventud.save(joven)
    return render( request, "juventud.html")

@login_required
def buscar_afiliado(request):
    if user_passes_test(lambda u: u.is_superuser):
        return render(request, "buscar_afiliado.html")
    else:
        HttpResponse("Lo sentimos, esta página sólo es accesible para administradores; si usted es un administrador y no puede acceder, póngase en contacto con el administrador de la página")

@login_required
def busqueda_afiliado(request):

    if user_passes_test(lambda u: u.is_superuser):
        if request.GET['nombre']:
        #respuesta= f"Se ha encontrado al afiliado: {request.GET['nombre'] }"
            nombre = request.GET['nombre']
            afiliados = afiliado.objects.filter(nombre=nombre)

            return render(request, "resultados_busqueda.html", {"afiliados":afiliados, "nombre":nombre})
        else:

            respuesta = "no enviaste datos"

        return HttpResponse(respuesta)

    else:
        HttpResponse("Lo sentimos, esta página sólo es accesible para administradores; si usted es un administrador y no puede acceder, póngase en contacto con el administrador de la página")
    

@login_required
def leer_afiliados(request):

    if user_passes_test(lambda u: u.is_superuser):
        afiliados = afiliado.objects.all()

        contexto = {"afiliados":afiliados}

        return render(request, "leer_afiliados.html", contexto)

    else:
        HttpResponse("Lo sentimos, esta página sólo es accesible para administradores; si usted es un administrador y no puede acceder, póngase en contacto con el administrador de la página")

@login_required
def eliminar_afiliado(request, id):
    
    if user_passes_test(lambda u: u.is_superuser):

        Afiliado = afiliado.objects.get(id=id)
        Afiliado.delete()

        afiliados = afiliado.objects.all()

        return render(request , "leer_afiliados.html" , {"afiliados":afiliados})

    else:
        HttpResponse("Lo sentimos, esta página sólo es accesible para administradores; si usted es un administrador y no puede acceder, póngase en contacto con el administrador de la página")


@login_required
def editar_afiliado(request, id):
    if user_passes_test(lambda u: u.is_superuser):
        Afiliado = afiliado.objects.get(id=id)

        if request.method == "POST":

            miFormulario = formulario_afiliados(request.POST)

        

            if miFormulario.is_valid():

                informacion = miFormulario.cleaned_data

                Afiliado.nombre = informacion['nombre']
                Afiliado.apellido = informacion['apellido']
                Afiliado.direccion = informacion['direccion']
                Afiliado.dni = informacion['dni']
                Afiliado.telefono = informacion['telefono']
                Afiliado.fecha_nacimiento = informacion['fecha_nacimiento']

                Afiliado.save()


            return render(request, 'leer_afiliados.html' , {"Afiliado":Afiliado})

        else:

            miFormulario = formulario_afiliados(initial={'nombre':Afiliado.nombre, 'apellido':Afiliado.apellido,  
        'direccion':Afiliado.direccion , 'dni':Afiliado.dni , 'telefono':Afiliado.telefono , 
        'fecha_nacimiento':afiliado.fecha_nacimiento})

        return render(request , "editar_afiliado.html", {"miFormulario":miFormulario, "Afiliado":Afiliado})

    else:
        HttpResponse("Lo sentimos, esta página sólo es accesible para administradores; si usted es un administrador y no puede acceder, póngase en contacto con el administrador de la página")

@login_required
def editar_perfil(request, id):

    usuario = User.objects.get(id=id)

    if request.method == 'POST':

        miFormulario = user_edit_form(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            usuario.save()

            return render(request, "index.html")

    else:

    

        miFormulario = user_edit_form(initial={ 'email':usuario.email})
    return render(request, "editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})


    
@user_passes_test(lambda u: u.is_superuser)
def agregar_proyecto(request):
    if request.method == "POST":
        Proyecto = proyecto( titulo=request.POST['titulo'], contenido=request.POST['contenido'], autor=request.POST['autor'], resumen=request.POST['resumen'])
        proyecto.save(Proyecto)
    return render( request, "agregar_proyecto.html")


@login_required
def eliminar_usuario(request, id):
    
    if user_passes_test(lambda u: u.is_superuser):

        Usuario = User.objects.get(id=id)
        Usuario.delete()

        usuarios = afiliado.objects.all()

        return render(request , "leer_usuarios.html" , {"usuarios":usuarios})

    else:
        HttpResponse("Lo sentimos, esta página sólo es accesible para administradores; si usted es un administrador y no puede acceder, póngase en contacto con el administrador de la página")


@login_required
def leer_usuario(request):

    if user_passes_test(lambda u: u.is_superuser):
        usuarios = User.objects.all()

        contexto = {"usuarios":usuarios}

        return render(request, "leer_usuarios.html", contexto)

    else:
        HttpResponse("Lo sentimos, esta página sólo es accesible para administradores; si usted es un administrador y no puede acceder, póngase en contacto con el administrador de la página")


def ver_proyecto(request, id):

    Proyecto = proyecto.objects.get(id=id)
    contexto = {"Proyecto":Proyecto} 

    return render(request , "leer_proyecto.html" , contexto,  )

   
@login_required
def editar_proyecto(request, id):
    if user_passes_test(lambda u: u.is_superuser):
        Proyecto = proyecto.objects.get(id=id)

        if request.method == "POST":

            miFormulario = formulario_proyectos(request.POST)

        

            if miFormulario.is_valid():

                informacion = miFormulario.cleaned_data

                Proyecto.titulo = informacion['titulo']
                Proyecto.contenido = informacion['contenido']
                Proyecto.autor = informacion['autor']
                Proyecto.resumen = informacion['resumen']

                Proyecto.save()


            return render(request, 'nuestros_proyectos.html' , {"Proyecto":Proyecto})

        else:

            miFormulario = formulario_proyectos(initial={'titulo':Proyecto.titulo, 'contenido':Proyecto.contenido,  
        'autor':Proyecto.autor , 'resumen':Proyecto.resumen})

        return render(request , "editar_proyecto.html", {"miFormulario":miFormulario, "Proyecto":Proyecto})

    else:
        HttpResponse("Lo sentimos, esta página sólo es accesible para administradores; si usted es un administrador y no puede acceder, póngase en contacto con el administrador de la página")


@login_required
def eliminar_proyecto(request, id):
    
    if user_passes_test(lambda u: u.is_superuser):

        Proyecto = proyecto.objects.get(id=id)
        Proyecto.delete()

        Proyecto = proyecto.objects.all()

        return render(request , "nuestros_proyectos.html" , {"Proyecto":Proyecto})

    else:
        HttpResponse("Lo sentimos, esta página sólo es accesible para administradores; si usted es un administrador y no puede acceder, póngase en contacto con el administrador de la página")


@login_required
def leer_proyectos(request):

    if user_passes_test(lambda u: u.is_superuser):
        proyectos = proyecto.objects.all()

        contexto = {"proyectos":proyectos}

        return render(request, "leer_proyectos.html", contexto)

    else:
        HttpResponse("Lo sentimos, esta página sólo es accesible para administradores; si usted es un administrador y no puede acceder, póngase en contacto con el administrador de la página")
