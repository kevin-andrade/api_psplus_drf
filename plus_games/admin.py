from django.contrib import admin
from plus_games.models import Jogo


class Jogos(admin.ModelAdmin):
    list_display = ['id', 'codigo_jogo', 'nome', 'plataforma_jogo', 'genero_jogo', 'classificacao', 'preco']
    list_display_links = ['id', 'codigo_jogo', 'nome', ]
    list_filter = ['plataforma_jogo', 'genero_jogo',  'classificacao']
    search_fields = ['nome', 'plataforma_jogo']
    list_per_page = 10
    
admin.site.register(Jogo, Jogos)