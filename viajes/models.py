from django.db import models

class Guia(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class PilotoCliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Viaje(models.Model):
    destino = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    kilometros = models.PositiveIntegerField()
    DIFICULTAD_CHOICES = [
            ('baja', 'Baja'),
            ('media', 'Media'),
            ('alta', 'Alta'),
        ]
    dificultad = models.CharField(max_length=10, choices=DIFICULTAD_CHOICES)
    # dificultad = models.CharField(max_length=50)
    # Un viaje tiene un solo guía, pero si el guía se elimina, el viaje no se borra (on_delete=models.SET_NULL)
    guia = models.ForeignKey(Guia, on_delete=models.SET_NULL, null=True, related_name="viajes")
    pilotos = models.ManyToManyField(PilotoCliente, related_name="viajes", blank=True)  # Opcional

    def __str__(self):
        return f"{self.destino} - {self.fecha}"
    