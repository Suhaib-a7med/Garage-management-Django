from django.contrib import admin

# Register your models here.
from .models import Mechanics, Reservations


admin.site.register(Mechanics)
admin.site.register(Reservations)