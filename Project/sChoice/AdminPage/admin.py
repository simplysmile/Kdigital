from django.contrib import admin
from AdminPage.models import Exercise,Food,ContactUs

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display=['ex_id','activity','aerobic','met','ex_name']
    
@admin.register(Food)

class FoodAdmin(admin.ModelAdmin):
    list_display=['f_NO','f_id','f_DB','f_name','f_por','f_carb','f_protein','f_fat']
    
@admin.register(ContactUs)

class ContactUs(admin.ModelAdmin):
    
    list_display=['c_No','c_name','c_email','c_tel','c_title','c_content']

