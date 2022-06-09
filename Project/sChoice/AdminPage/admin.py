from django.contrib import admin
from AdminPage.models import Exercise

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display=['ex_id','activity','aerobic','met','ex_name']


