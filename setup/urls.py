from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from cliente.views import ClienteViewSet

router = routers.DefaultRouter()
router.register('cliente', ClienteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
