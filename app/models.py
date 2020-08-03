from django.db import models

# Create your models here.
class Course(models.Model):
    cno=models.AutoField(primary_key=True)
    cname=models.CharField(max_length=64)
    faculty=models.CharField(max_length=64)
    class_date=models.DateField(default=True)
    class_time=models.CharField(max_length=54)
    fees=models.FloatField(max_length=34)
    duration=models.IntegerField()

class Student_data(models.Model):
    sid=models.AutoField(primary_key=True)
    sname=models.CharField(max_length=64)
    contactno=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=64)
class Enroll_data(models.Model):
    sname=models.CharField(max_length=64)
    cname=models.CharField(max_length=50)
    phno=models.IntegerField()



