from django.contrib import admin
from cliente.models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'rg', 'celular', 'ativo')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_filter = ('ativo',)
    list_editable = ('ativo',)
    list_per_page = 10

admin.site.register(Cliente, ClienteAdmin)
