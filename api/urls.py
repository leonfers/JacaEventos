from django.conf.urls import url, include

from api.core import views as core_views
from api.routers import router

urlpatterns = [
    url(r'^', include(router.urls)),

]