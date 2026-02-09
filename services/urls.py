from rest_framework.routers import DefaultRouter
from .views import ServiceViewset

router = DefaultRouter()
router.register(r'services', ServiceViewset)

urlpatterns = router.urls
