from rest_framework import routers
from .api import PersonaViewSet, TareaViewSet

router = routers.DefaultRouter()

router.register('api/task/persona', PersonaViewSet, 'persona')
router.register('api/task/tarea', TareaViewSet, 'tarea')

urlpatterns = router.urls

#urlpatterns = []
