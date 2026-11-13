from django.urls import path
from . import views

urlpatterns = [
	path('ahoj/', views.ahoj, name='ahoj'), 
    path('o-mne/', views.o_mne, name='o_mne'),
    path('rozvrh/', views.rozvrh, name='rozvrh'),
    path('pozdrav/', views.pozdrav, name='pozdrav'),
    path('sucet/', views.sucet, name='sucet'),
    path('kalkulacka/', views.kalkulacka, name='kalkulacka'),
    path('obdlznik/', views.obdlznik, name='obdlznik'),
    path('vek/', views.vek, name='vek'),
]