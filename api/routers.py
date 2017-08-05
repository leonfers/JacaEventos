from rest_framework.routers import DefaultRouter
from . import views
from .core import views as views_core
from .core.views import EventoViewSet,AtividadeViewSet
router = DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'eventos', views_core.EventoViewSet)
router.register(r'atividade', views_core.AtividadeViewSet)