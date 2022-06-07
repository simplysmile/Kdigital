from django.urls import path
from . import views
app_name='DailyCheck'
urlpatterns = [
    path('calendar/',views.calendar,name='calendar'),
    
]
