from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE , null=True)
    department = models.CharField(max_length=255)
    year = models.IntegerField()


    def __str__(self):
        return self.name

class Professor(models.Model): 
    name = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    department = models.CharField(max_length=100)
    email = models.EmailField(default='example@example.com')
    photo = models.ImageField(default=0, upload_to='professor_photos')
    phone_number = models.CharField(default=0, max_length=20)
    lab_number = models.CharField(default=0, max_length=20)

    def __str__(self):
        return self.name
class Assistant(models.Model):
    name = models.CharField(max_length=100) # 이름
    user = models.OneToOneField(User, on_delete=models.CASCADE , null=True)
    department = models.CharField(max_length=100) #학과
    lab_number = models.CharField(default=0 ,max_length=20) #학과사무실번호
    phone_number = models.CharField(default=0, max_length=20) #번호

    def __str__(self):
        return self.name
    
class TimeTable(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f'{self.professor.name} - {self.start_time} to {self.end_time}'

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('REQUESTED', 'Requested'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    time = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='REQUESTED')

    def __str__(self):
        return f'{self.student.name} appointment with {self.professor.name} - {self.status}'