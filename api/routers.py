from rest_framework.routers import DefaultRouter
from . import views
from .core import views as views2
from .core.views import EventoViewSet
router = DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'eventos', views2.EventoViewSet)