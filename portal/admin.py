from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Autor) # Registrar a class Autor do models na interface admin
admin.site.register(Livro) # Registrar a class Livro do models na interface admin
admin.site.register(Editora) # Registrar a class Editora do models na interface admin
admin.site.register(Formato) # Registrar a class Formato do models na interface admin
