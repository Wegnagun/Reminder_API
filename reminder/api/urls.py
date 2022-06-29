from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EventViewSet

router = DefaultRouter()
router.register('event', EventViewSet, basename='event')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
]
