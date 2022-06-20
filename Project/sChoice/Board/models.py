from django.db import models
from Member.models import Members

class MealBoard(models.Model):
    b_No=models.AutoField(primary_key=True)
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    m_Pro=models.CharField(max_length=100,blank=True)
    b_Title=models.CharField(max_length=1000)
    b_Content=models.TextField(blank=True)
    b_Group=models.IntegerField(default=0)
    b_Step=models.IntegerField(default=1)
    b_Indent=models.IntegerField(default=0)
    b_Hit=models.IntegerField(default=0)
    b_File=models.ImageField(blank=True,upload_to="images")
    b_Createdate=models.DateTimeField(auto_now_add=True)
    b_Modidate=models.DateTimeField(auto_now=True)
    
class ExerciseBoard(models.Model):
    b_No=models.AutoField(primary_key=True)
    member=models.ForeignKey(Members,on_delete=models.CASCADE)
    m_Pro=models.CharField(max_length=100,blank=True)
    b_Title=models.CharField(max_length=1000)
    b_Content=models.TextField(blank=True)
    b_Group=models.IntegerField(default=0)
    b_Step=models.IntegerField(default=1)
    b_Indent=models.IntegerField(default=0)
    b_Hit=models.IntegerField(default=0)
    b_File=models.ImageField(blank=True,upload_to="images")
    b_Createdate=models.DateTimeField(auto_now_add=True)
    b_Modidate=models.DateTimeField(auto_now=True)
    



