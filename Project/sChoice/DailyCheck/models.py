from django.db import models
# from Member.models import Members
# from AdminPage.models import Exercise

# class Dailyexercise(models.Model):
#     user=models.ForeignKey(Members,on_delete=models.CASCADE)
#     exercise=models.ForeignKey(Exercise,on_delete=models.CASCADE) # 운동이름
#     ex_time=models.IntegerField(default=0,blank=True) # 운동한 시간
#     burned_kcal=models.IntegerField(default=0,blank=True) # 운동해서 태운 칼로리
#     goal_kcal=models.IntegerField(default=1000,blank=True) # 내 운동 목표 칼로리
#     createdate=models.DateTimeField(auto_now_add=True) # 운동한 날짜