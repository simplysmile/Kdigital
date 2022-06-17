from django.contrib import admin
from DailyCheck.models import Dailyexercise,DailyMeal

@admin.register(Dailyexercise)
class DailyexerciseAdmin(admin.ModelAdmin):
    list_display=['ex_No','user','exercise','createdate']
    
    
@admin.register(DailyMeal)
class DailyMealAdmin(admin.ModelAdmin):
    list_display=['d_member','d_food_name','d_meal_date','d_meal_time']


