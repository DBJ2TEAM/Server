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

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    time = models.CharField(max_length=10,null=True)  # time 필드를 문자열 형식으로 변경
    day = models.CharField(max_length=20,null=True)  # day 필드 추가
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='REQUESTED')

    def __str__(self):
        return f'{self.student.name} appointment with {self.professor.name} - {self.status}'
class Room(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class RoomTimetable(models.Model):
    day = models.CharField(max_length=20)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day} {self.start_time} - {self.end_time}"

class RoomReservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    timetable = models.ForeignKey(RoomTimetable, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"Reservation: {self.room} - {self.start_time} to {self.end_time}"

    def is_overlapping(self):
        existing_reservation = RoomReservation.objects.filter(
            Q(room=self.room) & Q(timetable=self.timetable) &
            (
                Q(start_time__lt=self.end_time, end_time__gt=self.start_time) |
                Q(start_time__gte=self.end_time, end_time__lte=self.start_time)
            )
        ).exists()

        return existing_reservation