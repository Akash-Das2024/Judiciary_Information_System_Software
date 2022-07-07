from django.urls import path
from . import views

urlpatterns = [
    path('',views.judge,name = "judge"),
]