from django.db import models
from django.contrib.auth.models import User
# Create your models here

class teacherChart(models.Model):
    user =  models.OneToOneField(User, on_delete=models.CASCADE)
    AuburnID = models.CharField(blank = True,max_length = 50)
    
    
    
    class Meta:
            verbose_name_plural = "TeacherChart"

class Picture(models.Model):
    picture = models.ImageField(upload_to='pictures/')