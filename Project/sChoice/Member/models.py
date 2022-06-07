from pyexpat import model
from django.db import models
from PIL import Image

class Members(models.Model):
    user_id = models.CharField(max_length=20,primary_key=True)
    user_pw = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    pro = models.IntegerField(default=0)
    birth = models.DateField(blank=True)
    gender = models.CharField(max_length=10,blank=True)
    phone = models.CharField(max_length=13,blank=True)
    zipcode = models.CharField(max_length=6,blank=True)
    addressd1=models.CharField(max_length=1000,blank=True)
    addressd2=models.CharField(max_length=1000,blank=True)
    user_purpose = models.CharField(max_length=1000,blank=True)
    service = models.CharField(max_length=1000,blank=True)
    vegan = models.IntegerField(default=0)
    allergic_food = models.CharField(max_length=1000,blank=True)
    goal_wieght = models.IntegerField(default=55)
    goal_bodyfat = models.IntegerField(default=25)
    createdate=models.DateTimeField(auto_now_add=True)
    modidate=models.DateTimeField(auto_now=True)
    
class Dailydata(models.Model):
    user = models.ForeignKey(Members,on_delete=models.CASCADE)
    height = models.IntegerField(blank=True)
    cur_weight = models.IntegerField(blank=True)
    cur_bodyfat = models.IntegerField(blank=True)
    cur_neck = models.IntegerField(blank=True)
    cur_waist = models.IntegerField(blank=True)
    cur_hip = models.IntegerField(blank=True)
    day_img = models.ImageField(blank=True)
    ex_level = models.CharField(max_length=100,blank=True)
    week_ex = models.IntegerField(default=0)
    day_ex = models.IntegerField(default=0)
    focus_ex = models.CharField(max_length=1000,blank=True)
    