from django.db import models
from django.core.validators import MinValueValidator

class Alumna(models.Model):
    nombre = models.CharField(max_length=50),
    apellido = models.CharField(max_length=50),
    curso = models.CharField(max_length=10),

    def __str__(self):
        return f"Alumna: {self.nombre} {self.apellido}"

class Tarjeta(models.Model):
    codigo = models.CharField(max_length=15,unique=True),
    saldo = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(-2000)]),
    id_alumna = models.ForeignKey(Alumna, on_delete=models.CASCADE)
    fecha_activacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tarjeta: {self.codigo} / Saldo: $ {self.saldo}"

class Producto(models.Model):
    nombre = models.CharField(max_length=15),
    marca = models.CharField(max_length=15),
    precio = models.DecimalField(max_digits=8, decimal_places=2),
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.nombre} {self.marca}/ Precio: $ {self.precio}/ Stock: {self.stock}"

