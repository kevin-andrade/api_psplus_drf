from rest_framework import serializers

from plus_games.models import Jogo


class JogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jogo
        fields = '__all__'