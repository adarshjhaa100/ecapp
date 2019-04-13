from django.urls import path,include
from . import views

urlpatterns = [
path('searchStation/',views.searchStation,name='searchStation'),
path('allStations/',views.stationAll,name='allStations'),
path('allCandidates/',views.ViewAllCandidate,name='allCandidates'),
path('getCandidate/',views.getCandidate,name='getCandidate'),
path('getpwd/',views.getPwd),
path('getThrd/',views.getThrd),
path('getSuggestion/',views.getSuggestion),
path('getResults/',views.getResults),
path('update/',views.up)

]
