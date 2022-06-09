from django.contrib import admin
from DailyCheck.models import Dailyexercise

@admin.register(Dailyexercise)
class DailyexerciseAdmin(admin.ModelAdmin):
    list_display=['user','exercise','createdate']


