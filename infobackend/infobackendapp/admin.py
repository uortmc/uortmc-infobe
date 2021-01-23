from django.contrib import admin
from . import models
# Register your models here.

admin.register(models.Doctor)
admin.register(models.Patient)
admin.register(models.Scan)

