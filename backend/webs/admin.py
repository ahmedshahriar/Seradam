from django.contrib import admin

# Register your models here.
from .models import Ryans, Startech, Mapping
admin.site.register(Ryans)
admin.site.register(Startech)
admin.site.register(Mapping)