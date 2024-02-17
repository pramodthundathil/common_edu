from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    course  = models.CharField(max_length = 255)
    def __str__(self):
        return self.course

class RecruiterData(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    profile = models.CharField(max_length = 255)
    conmpany_logo_or_photo = models.FileField(upload_to="company_photo")
    field_of_work = models.CharField(max_length = 255)
    approval_status  = models.BooleanField(default = False)

    def __str__(self):
        return str(self.user) + str(self.field_of_work)
    
class Education(models.Model):
    user  = models.ForeignKey(User,on_delete = models.CASCADE,null = True, blank = True)
    stream = models.CharField(max_length = 255)
    institution = models.CharField(max_length = 255)
    year = models.IntegerField()
    CGPA = models.CharField(max_length = 20)

class Experiance(models.Model):
    user  = models.ForeignKey(User,on_delete = models.CASCADE,null = True, blank = True)
    Designation = models.CharField(max_length = 255)
    Company = models.CharField(max_length = 255)
    startyear = models.IntegerField()
    Endyear = models.CharField(max_length = 20)
    

class StudentProfile(models.Model):
    user  = models.ForeignKey(User,on_delete = models.CASCADE,null = True, blank = True)
    last_name = models.CharField(max_length = 255)
    Phone_number = models.IntegerField()
    address = models.CharField(max_length = 1000)
    Bio_Discription = models.CharField(max_length = 2000)
    Skills = models.CharField(max_length = 1000)
    Languages = models.CharField(max_length = 255)
    resume = models.FileField(upload_to="Student_resumes", null=True)
    Photo = models.FileField(upload_to = "student_photo",blank=True)
    course = models.ForeignKey(Course,on_delete = models.CASCADE, null = True, blank = True)
    approval_status = models.BooleanField(default = False)


class TeacherProfile(models.Model):
    user  = models.ForeignKey(User,on_delete = models.CASCADE,null = True, blank = True)
    last_name = models.CharField(max_length = 255)
    Phone_number = models.IntegerField()
    address = models.CharField(max_length = 1000)
    course = models.ForeignKey(Course,on_delete = models.CASCADE, null = True, blank = True)
    Photo = models.FileField(upload_to = "student_photo",blank=True)
    approval_status = models.BooleanField(default = False)


class ResumeWritingTips(models.Model):
    tip_title = models.CharField(max_length = 255)
    tip = models.CharField(max_length=255)
    date = models.DateField(auto_now_add = True)



