from rest_framework import routers
from .api import PersonaViewSet

router = routers.DefaultRouter()

router.register('api/task', PersonaViewSet, 'persona')


urlpatterns = router.urls

#urlpatterns = []
