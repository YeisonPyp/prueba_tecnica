from rest_framework import routers
from .api import PersonaViewSet

router = routers.DefaultRouter()

router.register('api/task/persona', PersonaViewSet, 'persona')
router.register('api/task/tarea', PersonaViewSet, 'tarea')

urlpatterns = router.urls

#urlpatterns = []
