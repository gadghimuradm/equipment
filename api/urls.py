from django.urls import path, include
from rest_framework import routers

from api.views.auth import CustomAuthToken, LogoutView
from api.views.equipment import EquipmentViewSet, EquipmentTypeViewSet

equipment_router = routers.SimpleRouter()
equipment_router.register('equipment', EquipmentViewSet)
equipment_router.register('equipment-type', EquipmentTypeViewSet)

urlpatterns = [
    # Auth
    path('user/login/', CustomAuthToken.as_view()),
    path('user/logout/', LogoutView.as_view()),
    path('', include(equipment_router.urls)),
]
