from django.db import models

class EquipoElectronico(models.Model):
    equipo = models.CharField(
        max_length=150, 
        verbose_name="Nombre del Equipo"
    )
    marca_specs = models.TextField(
        verbose_name="Marca y Especificaciones"
    )
    precio_venta = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Precio de Venta ($ COP)"
    )
    garantia_activa = models.BooleanField(
        default=True, 
        verbose_name="¿Garantía Activa?"
    )

    class Meta:
        verbose_name = "Equipo Electrónico"
        verbose_name_plural = "Equipos Electrónicos"
        ordering = ['-precio_venta']

    def __str__(self):
        return f"{self.equipo} - ${self.precio_venta}"