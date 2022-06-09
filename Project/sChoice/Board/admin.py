from django.contrib import admin
from .models import MealBoard,ExerciseBoard

@admin.register(MealBoard)
class MealBoardAdmin(admin.ModelAdmin):
    list_display=[
        'b_No','b_Title','member','b_Createdate','b_Modidate'
    ]

@admin.register(ExerciseBoard)
class ExerciseBoardAdmin(admin.ModelAdmin):
    list_display=[
        'b_No','b_Title','member','b_Createdate','b_Modidate'
    ]

