from django.contrib import admin
from django.urls import path,include
from filmyhub_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('hollywood',views.hollywood,name='hollywood'),
    path('bollywood',views.bollywood,name='bollywood'),
    path('top_imdb',views.top_imdb,name='top_imdb'),
    path('contact',views.contact1,name='contact') 
    
]
