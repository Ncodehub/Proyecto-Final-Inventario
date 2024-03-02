from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .models import *
from .forms import*
from django.views.generic import ListView, View
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin #para las clases
from django.contrib.auth.decorators import login_required #para las funciones 

# Create your views here.

def home(request):
    return render(request, "aplicacion/home.html") # le digo que busque en aplicacion un home.html

def conoceme(request):
    return render(request, "aplicacion/conoceme.html")

def buscar(request):
    return render(request, "aplicacion/buscar.html")

##--------------------------------Repuestos---------------------------------------------------
class RepuestosList(LoginRequiredMixin, ListView):
    model = Repuestos

class RepuestoCreate(LoginRequiredMixin, CreateView):
    model =  Repuestos
    fields = ['nombre', 'marca','precio', 'cantidad'] 
    success_url = reverse_lazy('repuestos')

class RepuestoUpdate(LoginRequiredMixin, UpdateView):
    model =  Repuestos
    fields = ['nombre', 'marca','precio', 'cantidad'] 
    success_url = reverse_lazy('repuestos')

class RepuestoDelete(LoginRequiredMixin, DeleteView):
    model =  Repuestos
    success_url = reverse_lazy('repuestos')

##--------------------------------Maquina---------------------------------------------------
class MaquinaList(LoginRequiredMixin, ListView):
    model = Maquina

class MaquinaCreate(LoginRequiredMixin, CreateView):
    model =  Maquina
    fields = ['nombre', 'marca','area'] 
    success_url = reverse_lazy('maquina')

class MaquinaUpdate(LoginRequiredMixin, UpdateView):
    model =  Maquina
    fields = ['nombre', 'marca','area'] 
    success_url = reverse_lazy('maquina')

class MaquinaDelete(LoginRequiredMixin, DeleteView):
    model =  Maquina
    success_url = reverse_lazy('maquina')

##--------------------------------Proveedores---------------------------------------------------
class ProveedorList(LoginRequiredMixin, ListView):
    model = Proveedores

class ProveedorCreate(LoginRequiredMixin, CreateView):
    model =  Proveedores
    fields = ['nombre', 'direccion','fono', 'email'] 
    success_url = reverse_lazy('proveedores')

class ProveedorUpdate(LoginRequiredMixin, UpdateView):
    model =  Proveedores
    fields = ['nombre', 'direccion','fono', 'email'] 
    success_url = reverse_lazy('proveedores')

class ProveedorDelete(LoginRequiredMixin, DeleteView):
    model =  Proveedores
    success_url = reverse_lazy('proveedores')
#_____________________________Solicitar Repuesto__________________________________________________________
class SolicitudRepuestoList(LoginRequiredMixin, ListView):
    model = SolicitarRepuestos

class SolicitudRepuestoCreate(LoginRequiredMixin, CreateView):
    model =  SolicitarRepuestos
    fields = ['nombre', 'marca', 'cantidad', 'fechasolicitud'] 
    success_url = reverse_lazy('solicitudrepuesto')

#__________________________________________ Buscar _______________________________________________________    

def buscarRepuestos(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        repuestos = Repuestos.objects.filter(nombre__icontains=patron)
        contexto = {"repuestos_list": repuestos }
        return render(request, "aplicacion/repuestos_list.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")

#_______________________________________Login - Registro__________________________________________________________

def login_request(request):
    if request.method == "POST":
        usuario = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=usuario, password=password)
        if user is not None:
            login(request, user)
            try:
                avatar= Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            return render(request, "aplicacion/home.html")
        else:
            return redirect(reverse_lazy('login'))
        python
    miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm })

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))

    else:    
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm }) 

#_______________________ Editar Perfil _______________________
@login_required
def editarPerfil(request):
    usuario = request.user

    if request.method == "POST":
        Form = UserEditForm(request.POST)
        if Form.is_valid():
            informacion = Form.cleaned_data
            user = User.objects.get(username = usuario)
            user.email = informacion['email']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.set_password(informacion['password1'])
            user.save()
            return redirect(reverse_lazy('home'))
    else:    
        form = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": form })

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            usuario = User.objects.get(username = request.user)
            #Para borrar avatar
            avatarViejo= Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range (len(avatarViejo)):
                    avatarViejo[i].delete()
            #_______________________________________#
            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            #_____________URL imagen____________________#
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"]= imagen
            return render(request, "aplicacion/home.html")
    else:    
        form = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": form })