# cargar_repuesto_app/models.py
from django.db import models
from django.contrib.auth.models import User
from deposito_app.models import Repuesto
import qrcode
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image, ImageDraw

class IngresoRepuesto(models.Model):
    jefe_deposito = models.ForeignKey(User, on_delete=models.CASCADE)
    repuesto = models.ForeignKey(Repuesto, on_delete=models.CASCADE)
    cantidad_ingresada = models.IntegerField()
    fecha_ingreso = models.DateField(auto_now_add=True)
    lote = models.CharField(max_length=20, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f"Repuesto: {self.repuesto.nombre}\n"
                    f"Cantidad: {self.cantidad_ingresada}\n"
                    f"Fecha de ingreso: {self.fecha_ingreso}\n"
                    f"Lote: {self.lote}")
        qr.make(fit=True)

        img = qr.make_image(fill='black', back_color='white')
        buffer = BytesIO()
        img.save(buffer, 'PNG')
        self.qr_code.save(f"qr_code_{self.id}.png", InMemoryUploadedFile(buffer, None, f"qr_code_{self.id}.png", 'image/png', buffer.tell(), None))
        super().save(*args, **kwargs)