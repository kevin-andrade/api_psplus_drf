from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls import static

from plus_games.views import JogosViewSet


router = routers.DefaultRouter()
router.register('Jogos', JogosViewSet, basename='Jogos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)