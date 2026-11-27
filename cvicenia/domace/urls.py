from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_domace, name='index_domace'),
    path('vizitka/', views.du2_vizitka, name='vizitka'), 
    path('teplota/', views.du3_teplota, name='teplota'),
]