from django.db import models

# School Name,School City,Chapter Name,Chapter ID,Division,Region,District,FirstName,MI,LastName,Member ID,MemberType,GPA,GradYear,NumYears,BusEdCourse,EMail,Paid

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    region = models.IntegerField()
    district = models.IntegerField()

class Student(models.Model):
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    school = models.ForeignKey(School)
    member_id = models.CharField(max_length=200)
    gpa = models.FloatField()
    grad_year = models.IntegerField()
    num_years = models.IntegerField()
    courses = models.CharField(max_length=200)
    paid = models.BooleanField()
