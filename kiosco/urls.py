from django.urls import path
from kiosco.views import *

urlpatterns = [
    path("",home, name="home")
]