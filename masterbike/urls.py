from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('porhacer', views.porhacer, name='porhacer'),
    path('arriendo', views.arriendo, name='arriendo'),
]
