from pyexpat import model
from django.db import models
from PIL import Image

class Members(models.Model):
    user_id = models.CharField(max_length=20,primary_key=True)
    user_pw = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    pro_Choice=((0,'비전문가'),(1,'전문가'))
    pro = models.IntegerField(default=0,choices=pro_Choice)
    birth = models.DateField(blank=True)
    gender_Choice=(('M','남자'),('F','여자'))
    gender = models.CharField(max_length=10,choices=gender_Choice,blank=True)
    phone = models.CharField(max_length=13,blank=True)
    email = models.CharField(max_length=1000,blank=True)
    zipcode = models.CharField(max_length=6,blank=True)
    addressd1=models.CharField(max_length=1000,blank=True)
    addressd2=models.CharField(max_length=1000,blank=True)
    purpose_Choice=(('abs','복부'),('shoulders','어깨'),('arms','팔'),('back','등'),('chest','가슴'),('legs','하체'),('all','전신'))
    user_purpose = models.CharField(max_length=1000,choices=purpose_Choice,blank=True) # 신체 타켓부위 (복부,하체,상체)
    service_Choice=(('meal','식단형'),('balance','균형형'),('exercise','운동형'))
    service = models.CharField(max_length=1000,choices=service_Choice,blank=True)
    vegan_Choice=(('vegan','비건채식'),('lacto','락토채식'),('ovo','오보채식'),('lactoovo','락토오보채식'),('pollo','폴로채식'),('pesco','페스코채식'),('flexitarian','플렉시테리안'),('notvegan','해당사항없음'))
    vegan = models.CharField(max_length=100,choices=vegan_Choice,blank=True)
    allergic_food = models.CharField(max_length=1000,blank=True)
    goal_weight = models.IntegerField(default=55,blank=True)
    goal_bodyfat = models.IntegerField(default=25,blank=True)
    goal_period = models.IntegerField(default=30,blank=True)
    createdate=models.DateTimeField(auto_now_add=True)
    modidate=models.DateTimeField(auto_now=True)
    
class Dailydata(models.Model):
    user = models.ForeignKey(Members,on_delete=models.CASCADE)
    height = models.IntegerField(blank=True)
    cur_weight = models.IntegerField(blank=True)
    cur_bmi=models.IntegerField(blank=True)
    cur_bodyfat = models.IntegerField(blank=True)
    cur_neck = models.IntegerField(blank=True)
    cur_waist = models.IntegerField(blank=True)
    cur_hip = models.IntegerField(blank=True)
    day_img = models.ImageField(blank=True)
    level_Choice=(('2','저강도 운동'),('3','중강도 운동'),('6','고강도 운동')) # 운동강도
    ex_level = models.CharField(max_length=100,choices=level_Choice,blank=True)
    week_ex = models.IntegerField(default=0,blank=True)
    day_ex = models.IntegerField(default=0,blank=True)    
    add_date=models.DateTimeField(auto_now_add=True)
    