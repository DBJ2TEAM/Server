from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    student_id = models.IntegerField(unique=True)
    year = models.IntegerField()

    def __str__(self):
        return self.name

class Professor(models.Model):
    name = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    lab = models.CharField(max_length=255)

    def __str__(self):
        return self.name
