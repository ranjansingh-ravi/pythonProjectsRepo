from django.urls import path
from . import views              # here . means to import from same directory

urlpatterns = [
    path("", views.first_app_home),
    path("simple_app/", views.simple_view),
    
    path('<int:num_page>/', views.news_page_view),
    path('<str:topic>/', views.news_view, name='topic_page'), # making the path dynamic 

    # path converter with argument type specified
    path('sum/<int:num1>/<int:num2>/' , views.add_view)
]


