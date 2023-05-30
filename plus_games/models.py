from django.db import models


class Jogo(models.Model):

    PLATAFORMA = (
        ('PS3', 'Playstation 3'),
        ('PS4', 'Playstation 4'),
        ('PS5', 'Playstation 5'),
        ('PC', 'Pc'),
    )

    GENERO = (
        ('ACAO', 'Ação'),
        ('AVENTURA', 'Aventura'),
        ('ARCADE', 'Arcade'),
        ('TIRO', 'Tiro'),
        ('RPG', 'RPG'),
        ('SIMULACAO', 'Simulação'),
        ('ESPORTE', 'Esporte'),
        ('CORRIDA', 'Direção/Corrida'),
        ('TERROR', 'Terror'),
    )

    VOZES = (
        ('EN', 'Inglês'),
        ('BR', 'Português Brasil'),
        ('ES', 'Espanhol'),
    )

    CLASSIFICACAO_JOGO = (
        ('L', 'para todas as idades'),
        ('10', 'Classificação 10+'),
        ('12', 'Classificação 12+'),
        ('14', 'Classificação 14+'),
        ('16', 'Classificação 16+'),
        ('18', 'Classificação 18+'),
    )

    codigo_jogo = models.CharField(max_length=10, null=False, blank=False, unique=True)
    nome = models.CharField(max_length=100, blank=False, null=False, unique=True)
    plataforma_jogo = models.CharField(choices=PLATAFORMA, max_length=3, default='PS4')
    lancamento = models.DateField()
    distribuidora = models.CharField(max_length=100, null=False, blank=False)
    genero_jogo = models.CharField(choices=GENERO, max_length=10, default='')
    classificacao = models.CharField(choices=CLASSIFICACAO_JOGO, max_length=2, null=False, blank=False, default='')
    voz = models.CharField(choices=VOZES , max_length=2, blank=True, null=True)
    preco = models.FloatField()
    imagem = models.ImageField(blank=True)

    def __str_(self):
        return self.nome
