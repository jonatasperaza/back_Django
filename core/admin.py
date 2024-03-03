from django.contrib import admin

from .models import Categoria, Pais, tipoAtuacao, Produtora, Membros, Filme, atuacao

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Pais)
admin.site.register(tipoAtuacao)
admin.site.register(Produtora)
admin.site.register(Membros)
admin.site.register(Filme)
admin.site.register(atuacao)
