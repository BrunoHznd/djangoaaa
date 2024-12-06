from django.contrib import admin
from meuApp.models import Produto, Categoria

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'categoria')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)
