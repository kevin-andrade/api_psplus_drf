from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from plus_games.views import JogosViewSet


router = routers.DefaultRouter()
router.register('Jogos', JogosViewSet, basename='Jogos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
