from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet
from .views import DisponibilitesAPIView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/disponibilites/', DisponibilitesAPIView.as_view(), name='disponibilites-api'),
]

