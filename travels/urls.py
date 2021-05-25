from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index',views.index),
    path('destinations/<country>/<city>',views.destination, name="destinations"),
    path('destinations/<country>',views.destination_country, name="destinations_country")

    #path('search',views.search,name="search")
]
