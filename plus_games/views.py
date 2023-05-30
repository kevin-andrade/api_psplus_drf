from rest_framework import viewsets, generics

from plus_games.models import Jogo
from plus_games.serializers import JogoSerializer


class JogosViewSet(viewsets.ModelViewSet):
    '''Exibindo todos os Jogos Cadastrados'''
    queryset = Jogo.objects.all()
    serializer_class = JogoSerializer