from django.urls import path
from . import views
app_name='DailyCheck'
urlpatterns = [
    path('calendar/',views.calendar,name='calendar'),
    path('calendarData/',views.calendarData,name='calendarData'),
    path('<str:sdate>/mealCheck/',views.mealCheck,name='mealCheck'),
    path('<str:sdate>/exerciseCheck/',views.exerciseCheck,name='exerciseCheck'),
    path('<str:sdate>/<int:ex_no>/exerciseView/',views.exerciseView,name='exerciseView'),
    path('<str:sdate>/<int:ex_no>/exerciseUpdate/',views.exerciseUpdate,name='exerciseUpdate'),
    path('<str:sdate>/<int:ex_no>/exerciseDelete/',views.exerciseDelete,name='exerciseDelete'),
    path('health_result/',views.health_result,name='health_result'),
    path('aerobic/',views.aerobic,name='aerobic'),
    path('anaerobic/',views.anaerobic,name='anaerobic'),
    path('exercise1/',views.exercise1,name='exercise1'),
    path('exercise2/',views.exercise2,name='exercise2'),
    path('<str:sdate>/saveBtn/',views.saveBtn,name='saveBtn'),
    path('<str:sdate>/imgCheck/',views.imgCheck,name='imgCheck'),
    path('<str:sdate>/imgDelete/',views.imgDelete,name='imgDelete'),
    path('myStatus/',views.myStatus,name='myStatus'),
    path('myStatusData/',views.myStatusData,name='myStatusData'),
    path('selfCheck/',views.selfCheck,name='selfCheck'),
    path('searchMeal/',views.searchMeal,name='searchMeal'),
    path('<str:sdate>/addMealData/',views.addMealData,name='addMealData'),
    path('setGoals/',views.setGoals,name='setGoals'),
    path('delDailyMealData/',views.delDailyMealData,name='delDailyMealData')
    
]
