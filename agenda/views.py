from typing import Any
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.db.models import QuerySet
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from agenda.models import Contact
from agenda.models import Usuario
from django.contrib import messages
from django.contrib.auth.hashers import make_password

from django.shortcuts import render, redirect
from .models import Usuario
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def login_view(request):
       if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')


        # Verificar si el email ya está registrado en la tabla Usuario
        usuarios_existente = Usuario.objects.filter(email=email)

        if usuarios_existente.exists():
            return render(request, 'agenda/login.html', {'error': 'El email ya está registrado'})

    
        # Crear un nuevo usuario y guardar en la base de datos
        hashed_password = make_password(password)
        nuevo_usuario = Usuario(email=email, password=hashed_password)
        nuevo_usuario.save()

        messages.success(request, 'Registro exitoso. Te has registrado correctamente.')
        return redirect('contacto/')  # Redirigir a la página deseada después del registro exitoso

       return render(request, 'agenda/login.html')



class ContactListView(generic.ListView):
    model = Contact
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return Contact.objects.filter(name__icontains=q)

        return super().get_queryset()


class ContactCreateView(generic.CreateView):
    model = Contact
    fields = ('avatar', 'name', 'email', 'birth', 'phone',)
    success_url = reverse_lazy('contact_list')


class ContactUpdateView(generic.UpdateView):
    model = Contact
    fields = ('avatar', 'name', 'email', 'birth', 'phone',)
    success_url = reverse_lazy('contact_list')


class ContactDeleteView(generic.DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')
