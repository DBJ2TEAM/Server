from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE , null=True)
    department = models.CharField(max_length=255)
    student_id = models.IntegerField(unique=True)
    year = models.IntegerField()

    def __str__(self):
        return self.name

class Professor(models.Model): 
    name = models.CharField(max_length=100) # 이름
    department = models.CharField(max_length=100) #학과
    email = models.EmailField(default='example@example.com') #이메일
    photo = models.ImageField(default= 0 ,upload_to='professor_photos')
    phone_number = models.CharField(default=0, max_length=20) #번호
    lab_number = models.CharField(default=0 ,max_length=20) #연구실번호

    def __str__(self):
        return self.name
