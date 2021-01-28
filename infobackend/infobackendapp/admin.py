from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Doctor)
admin.site.register(models.Patient)
admin.site.register(models.Scan)
admin.site.register(models.Notification)

