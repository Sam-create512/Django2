from django.urls import path
from . import views

urlpatterns = [
	path('', views.cv1_index, name='cv1_index'), 
    path('obchod/', views.cv1_obchod, name='cv1_obchod'),
    path('body/', views.cv1_body, name='cv1_body'),
]