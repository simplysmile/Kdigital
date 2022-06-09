from django.contrib import admin
from .models import Members, Dailydata

@admin.register(Members)
class MembersAdmin(admin.ModelAdmin):
    list_display=[
        'user_id','user_name','pro','createdate','modidate'
    ]

@admin.register(Dailydata)
class DailydataAdmin(admin.ModelAdmin):
    list_display=[
        'user','height','cur_weight','add_date'
    ]