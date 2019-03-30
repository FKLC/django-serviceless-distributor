from django.urls import path
from serviceless_distributor import Distributor

from . import views

urlpatterns = [path("", views.event_receiver)]
