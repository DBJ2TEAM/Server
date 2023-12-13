from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
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
    

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('REQUESTED', 'Requested'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )
    
    requester = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    receiver = models.ForeignKey(Professor, on_delete=models.CASCADE,null=True)
    time = models.CharField(max_length=10,null=True)  # time 필드를 문자열 형식으로 변경
    day = models.CharField(max_length=20,null=True)  # day 필드 추가
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='REQUESTED')

    def __str__(self):
        return f'{self.student.name} appointment with {self.professor.name} - {self.status}'
class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class RoomReservation(models.Model):
    STATUS_CHOICES = (
        ('REQUESTED', 'Requested'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )
    requester = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    receiver = models.ForeignKey(Assistant, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='REQUESTED')
    day = models.CharField(max_length=10 , null=True)  # 요일을 문자열로 저장 (예: Monday)
    time = models.CharField(max_length=10,null=True)  # 시간을 문자열로 저장 (예: 11:00)

    def __str__(self):
        return f'{self.room.name} - {self.day} {self.time} - {self.status}'
    
class Equipment(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    STATUS_CHOICES = (
        ('REQUESTED', 'Requested'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    )

    requester = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    receiver = models.ForeignKey(Equipment, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='REQUESTED')
    day = models.CharField(max_length=10)  # 요일을 문자열로 저장 (예: Monday)
    time = models.CharField(max_length=10)  # 시간을 문자열로 저장 (예: 11:00)

    def __str__(self):
        return f'{self.receiver.name} - {self.day} {self.time} - {self.status}'