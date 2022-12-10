from django.urls import path
from .views import inicio, familiar

urlpatterns = [
    path("inicio/",inicio,name="inicio"),
    path("familia/", familiar, name="familiares"),

]