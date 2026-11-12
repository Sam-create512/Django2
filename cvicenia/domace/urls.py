from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('du2_vizitka/', views.du2_vizitka, name='du2_vizitka'), 
]