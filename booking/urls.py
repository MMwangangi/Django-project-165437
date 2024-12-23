from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FlightViewSet, PassengerViewSet, UserCreate

router = DefaultRouter()
router.register(r'flights', FlightViewSet)
router.register(r'passengers', PassengerViewSet)

urlpatterns = [
    path('register/', UserCreate.as_view(), name='user_create'),
] + router.urls