from django.urls import path
from . import views
app_name='DailyCheck'
urlpatterns = [
    path('calendar/',views.calendar,name='calendar'),
    path('mealCheck/',views.mealCheck,name='mealCheck'),
    path('exerciseCheck/',views.exerciseCheck,name='exerciseCheck'),
    
]
