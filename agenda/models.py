from django.db import models

# Create your models here.
class Contact(models.Model):
    avatar = models.ImageField(upload_to='contact', null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='Nombre')
    email = models.EmailField(max_length=50)
    birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    email = models.EmailField(unique=True)  # Usar unique=True para evitar duplicados
    password = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.email
