from django.urls import path
from .views import responseView

urlpatterns = [
    path("", responseView, name="home"),
]