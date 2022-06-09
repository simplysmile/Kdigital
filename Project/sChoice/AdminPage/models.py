from django.db import models

class Exercise(models.Model):
    # ex_no=models.AutoField()
    ex_id=models.CharField(max_length=10,primary_key=True) # 운동아이디
    # activity_Choice=(('bicycling','자전거'),('conditioning',''),('healthclub','헬스'),('running','러닝'),('sports',''),('walking','걷기'),('water','수상운동'),('winter','설상운동'))
    activity=models.CharField(max_length=1000,blank=True) # 운동종류
    # aerobic_Choice=(('o','유산소'),('x','무산소'))
    aerobic=models.CharField(max_length=1,blank=True) # 유산소, 무산소
    met=models.IntegerField(default=0,blank=True) # 에너지소모량
    # level_Choice=((2,'저강도 운동'),(3,'중강도 운동'),(6,'고강도 운동')) # 운동강도
    level = models.IntegerField(default=0,blank=True) # 운동강도
    ex_name=models.CharField(max_length=1000,blank=True) # 운동이름
    target_category=models.CharField(max_length=1000,blank=True) # 타켓 카테고리
    muscle=models.CharField(max_length=1000,blank=True) # 자극되는 근육
    equipment=models.CharField(max_length=1000,blank=True) # 운동에 사용되는 운동기구
    imgUrl=models.ImageField(blank=True) # 이미지 주소
