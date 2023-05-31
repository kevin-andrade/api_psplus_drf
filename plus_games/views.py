from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from plus_games.models import Jogo
from plus_games.serializers import JogoSerializer


class JogosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os Jogos Cadastrados'''
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', 'plataforma_jogo', 'preco']
    search_fields = ['codigo_jogo', 'nome', 'distribuidora']
    filterset_fields = ['plataforma_jogo', 'genero_jogo', 'classificacao']
