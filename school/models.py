from django.db import models

# School Name,School City,Chapter Name,Chapter ID,Division,Region,District,FirstName,MI,LastName,Member ID,MemberType,GPA,GradYear,NumYears,BusEdCourse,EMail,Paid

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    division = models.CharField(max_length=200)
    region = models.IntegerField(blank=True, null=True)
    district = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return u"%s" % self.name

class Member(models.Model):
    first = models.CharField(max_length=200)
    last = models.CharField(max_length=200)
    school = models.ForeignKey(School)
    memberid = models.CharField(max_length=200)
    membertype = models.CharField(max_length=200)
    gpa = models.FloatField(blank=True, null=True)
    grad_year = models.IntegerField(blank=True, null=True)
    num_years = models.IntegerField(blank=True, null=True)
    courses = models.CharField(max_length=200, blank=True, null=True)
    paid = models.BooleanField(default=False)
    
    def __unicode__(self):
        return u"%s %s" % (self.first, self.last)
