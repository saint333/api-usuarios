from rest_framework import routers
from .api import UsuarioViewSet

router = routers.DefaultRouter()

router.register('api/v1/projects',UsuarioViewSet,'projects')

urlpatterns = router.urls