from django.contrib import admin
from .models import Categoria, Produto, Cesta, Padaria, Email

# Register your models here.
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Cesta)
admin.site.register(Padaria)
admin.site.register(Email)