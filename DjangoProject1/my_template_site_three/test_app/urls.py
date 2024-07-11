from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.example_view),
    path('variable/', views.variable_view)
]