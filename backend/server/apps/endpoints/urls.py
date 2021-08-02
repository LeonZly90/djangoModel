from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from backend.server.apps.endpoints.views import EndpointViewSet
from backend.server.apps.endpoints.views import MLAlgorithmViewSet
from backend.server.apps.endpoints.views import MLAlgorithmStatusViewSet
from backend.server.apps.endpoints.views import MLRequestViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    url(r"^api/v1/", include(router.urls)),
]