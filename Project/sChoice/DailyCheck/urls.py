from django.urls import path
from . import views
app_name='DailyCheck'
urlpatterns = [
    path('calendar/',views.calendar,name='calendar'),
    path('mealCheck/',views.mealCheck,name='mealCheck'),
    path('exerciseCheck/',views.exerciseCheck,name='exerciseCheck'),
    path('exercise1/',views.exercise1,name='exercise1'),
    path('myStatus/',views.myStatus,name='myStatus'),
    path('selfCheck/',views.selfCheck,name='selfCheck'),
    path('searchMeal/',views.searchMeal,name='searchMeal'),
    
]
