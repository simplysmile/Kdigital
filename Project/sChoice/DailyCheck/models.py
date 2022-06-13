from django.db import models
from Member.models import Members
from AdminPage.models import Exercise
from datetime import datetime

class Dailyexercise(models.Model):
    ex_No=models.AutoField(primary_key=True)
    user=models.ForeignKey(Members,on_delete=models.CASCADE,null=True)
    exercise=models.ForeignKey(Exercise,on_delete=models.CASCADE,null=True) # 운동이름
    ex_time=models.IntegerField(default=0,blank=True) # 운동한 시간
    burned_kcal=models.IntegerField(default=0,blank=True) # 운동해서 태운 칼로리
    goal_kcal=models.IntegerField(default=1000,blank=True) # 내 운동 목표 칼로리
    content=models.TextField(blank=True)
    createdate=models.DateTimeField(default=datetime.now(),blank=True) # 운동한 날짜