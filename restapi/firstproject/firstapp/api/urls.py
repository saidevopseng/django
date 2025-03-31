from django.urls import path,include
from rest_framework import routers
from firstapp.api.views import HydJobsCRUDCBV
router=DefaultRouter()
router.register('hydjobsinfo',HydJobsCRUDCBV)

urlpatterns = [
    path('',include(router.urls)),
]