from django.urls import path, include
from . import views

app_name = 'test_app'

urlpatterns = [
    path('', views.example_view, name= 'index'),
    path('variable/', views.variable_view, name= 'variable')
]