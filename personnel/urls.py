from django.urls import path
# from .views import FlightView, ReservationView
from rest_framework import routers

router = routers.DefaultRouter()
# router.register("flights", FlightView)
# router.register("rezervations", ReservationView)

urlpatterns = [
    
]
urlpatterns += router.urls