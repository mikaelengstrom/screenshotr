from rest_framework import routers

from .viewsets import JobViewSet

router = routers.SimpleRouter()
router.register('jobs', JobViewSet)

urlpatterns = router.urls
