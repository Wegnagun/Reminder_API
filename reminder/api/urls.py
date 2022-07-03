from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BirthdayViewSet, EventViewSet, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('events', EventViewSet, basename='events')
router.register('birthdays', BirthdayViewSet, basename='birthdays')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
]
