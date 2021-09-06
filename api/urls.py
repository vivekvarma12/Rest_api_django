from django.urls import path
from .views import IdealWeight

urlpatterns = [
    path('idealweight/', IdealWeight),
]