from django.db import models
from Member.models import Members
from AdminPage.models import Exercise,Food
from datetime import datetime
from django.utils.timezone import now

class Dailyexercise(models.Model):
    ex_No=models.AutoField(primary_key=True)
    user=models.ForeignKey(Members,on_delete=models.CASCADE,null=True)
    exercise=models.ForeignKey(Exercise,on_delete=models.CASCADE,null=True) # 운동이름
    ex_time=models.IntegerField(default=0,blank=True) # 운동한 시간
    burned_kcal=models.IntegerField(default=0,blank=True) # 운동해서 태운 칼로리
    goal_kcal=models.IntegerField(default=1000,blank=True) # 내 운동 목표 칼로리
    content=models.TextField(blank=True)
    createdate=models.DateTimeField(default=now,editable=True) # 운동한 날짜
    
class DailyMeal(models.Model):
    d_No=models.AutoField(primary_key=True)
    d_member = models.ForeignKey(Members,on_delete=models.CASCADE,null=True) #member 외래키
    d_meal_date = models.DateTimeField(default=now,blank=True) #식사날짜
    mael_time_Choice=(('B','아침'),('L','점심'),('D','저녁'),('S','간식'))
    d_meal_time = models.CharField(max_length=10,choices=mael_time_Choice,null=True) #식사시간
    d_food = models.CharField(max_length=100,blank=True) #음식이름
    d_food_name = models.CharField(max_length=100,blank=True)
    d_por = models.IntegerField(default=0,blank=True) #1회제공량 
    d_carb = models.FloatField(default=0,blank=True) #탄수화물
    d_protein = models.FloatField(default=0,blank=True) #단백질
    d_fat = models.FloatField(default=0,blank=True) #지방
    d_kcal=models.IntegerField(default=0,blank=True) #칼로리
    d_img=models.ImageField(blank=True,upload_to="images")