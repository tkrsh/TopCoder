from django.urls import    path 
from . import views

app_name= 'main'

urlpatterns = [
path('homepage',views.homepage, name="homepage"),
path('',views.homepage, name="homepage"),
  
]