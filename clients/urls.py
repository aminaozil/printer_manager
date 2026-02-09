from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = router.urls