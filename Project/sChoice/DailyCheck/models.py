from django.db import models
from Member.models import Members

class Dailyexercise(models.Model):
    user=models.ForeignKey(Members,on_delete=models.CASCADE)
    ex_name=models.CharField(max_length=100)
    ex_time=models.IntegerField(default=0,blank=True)
    burned_kcal=models.IntegerField(default=0,blank=True)
    goal_kcal=models.IntegerField(default=1000,blank=True)
    createdate=models.DateTimeField(auto_now_add=True)