# from pyexpat import model
from django.db import models
from datetime import datetime, date
from django.utils.timezone import now
# from PIL import Image

class Members(models.Model):
    user_id = models.CharField(max_length=20,primary_key=True)
    user_pw = models.CharField(max_length=100,default=0)
    user_name = models.CharField(max_length=100,null=True)
    pro_Choice=(('notadvance','비전문가'),('advance','전문가'))
    pro = models.CharField(max_length=100,choices=pro_Choice,null=True)
    birth = models.DateField(default=date.today,null=True)
    gender_Choice=(('M','남자'),('F','여자'))
    gender = models.CharField(max_length=10,choices=gender_Choice,null=True)
    phone = models.CharField(max_length=13,null=True)
    email = models.CharField(max_length=1000,null=True)
    zipcode = models.CharField(max_length=6,null=True)
    addressd1=models.CharField(max_length=1000,null=True)
    addressd2=models.CharField(max_length=1000,null=True)
    addressd3=models.CharField(max_length=1000,null=True)
    purpose_Choice=(('weightlose','체중감소'),('maintain','체중유지'),('weightgain','체중증가'))
    user_purpose = models.CharField(max_length=1000,choices=purpose_Choice,null=True) # 신체 타켓부위 (복부,하체,상체)
    target_Choice=(('Abs','복부'),('Shoulders','어깨'),('Arms','팔'),('Back','등'),('Chest','가슴'),('Legs','하체'),('All','전신'))
    user_target = models.CharField(max_length=1000,choices=target_Choice,null=True) # 신체 타켓부위 (복부,하체,상체)
    service_Choice=(('meal','식단형'),('balance','균형형'),('exercise','운동형'))
    service = models.CharField(max_length=1000,choices=service_Choice,null=True)
    vegan_Choice=(('vegan','비건채식'),('lacto','락토채식'),('ovo','오보채식'),('lactoovo','락토오보채식'),('pollo','폴로채식'),('pesco','페스코채식'),('flexitarian','플렉시테리안'),('notvegan','해당사항없음'))
    vegan = models.CharField(max_length=100,choices=vegan_Choice,null=True)
    allergic_food = models.CharField(max_length=1000,null=True)
    goal_weight = models.IntegerField(default=55,null=True)
    goal_bodyfat = models.IntegerField(default=25,null=True)
    goal_period = models.IntegerField(default=30,null=True)
    createdate=models.DateTimeField(default=now,null=True)
    modidate=models.DateTimeField(default=now,null=True)
    
class Dailydata(models.Model):
    day_no=models.AutoField(primary_key=True)
    user = models.ForeignKey(Members,on_delete=models.CASCADE,null=True)
    height = models.FloatField(null=True)
    cur_weight = models.FloatField(null=True)
    cur_bmi=models.FloatField(null=True)
    cur_bodyfat = models.FloatField(null=True)
    cur_neck = models.FloatField(null=True)
    cur_waist = models.FloatField(null=True)
    cur_hip = models.FloatField(null=True)
    day_img = models.ImageField(null=True,blank=True,upload_to="images")
    level_Choice=(('2','저강도 운동'),('3','중강도 운동'),('6','고강도 운동')) # 운동강도
    ex_level = models.CharField(max_length=100,choices=level_Choice,null=True)
    week_ex = models.IntegerField(default=0,null=True)
    day_ex = models.IntegerField(default=0,null=True)    
    add_date=models.DateTimeField(default=now,null=True)
    goal_eat_kcal=models.IntegerField(default=1000,null=True)
    goal_burn_kcal=models.IntegerField(default=0,null=True)
    