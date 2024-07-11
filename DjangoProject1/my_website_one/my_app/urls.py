from django.urls import path  #path would help link path with functions
from . import views #can also write as from views import index but for more than one function 
                    # this is better

urlpatterns  = [
    path('', views.index, name="index")
]