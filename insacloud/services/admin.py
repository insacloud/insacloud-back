from django.contrib import admin
from services.models import Event, Picture, Mosaic, Mosaic_cell

# Register your models here.
admin.site.register(Event)
admin.site.register(Picture)
admin.site.register(Mosaic)
admin.site.register(Mosaic_cell)