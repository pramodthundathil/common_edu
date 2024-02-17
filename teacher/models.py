from django.db import models
from Home.models import StudentProfile, TeacherProfile

# Create your models here.
class Exam(models.Model):
   exam_name = models.CharField(max_length=50)
   teacher = models.ForeignKey(TeacherProfile, on_delete = models.CASCADE)
   question_number = models.PositiveIntegerField(null = True)
   expery = models.DateTimeField(auto_now_add = False, null=True)
   total_marks = models.PositiveIntegerField(null = True)
   def __str__(self):
        return self.exam_name

class Question(models.Model):
    course=models.ForeignKey(Exam,on_delete=models.CASCADE, null = True)
    marks=models.PositiveIntegerField()
    question=models.CharField(max_length=600)
    option1=models.CharField(max_length=200)
    option2=models.CharField(max_length=200)
    option3=models.CharField(max_length=200)
    option4=models.CharField(max_length=200)
    cat=(('Option1','Option1'),('Option2','Option2'),('Option3','Option3'),('Option4','Option4'))
    answer=models.CharField(max_length=200,choices=cat)

class Result(models.Model):
    student = models.ForeignKey(StudentProfile,on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam,on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    approval = models.BooleanField(default = False)

class Meterials(models.Model):
    teacher = models.ForeignKey(TeacherProfile,on_delete = models.CASCADE, null = True)
    Title = models.CharField(max_length=255)
    description = models.CharField(max_length = 255)
    Banner_image =models.FileField(upload_to="Bannerimage")
    Metirial = models.FileField(upload_to="Meterials")

class Videostudylink(models.Model):
    teacher = models.ForeignKey(TeacherProfile,on_delete = models.CASCADE, null = True)
    Title = models.CharField(max_length=255)
    description = models.CharField(max_length = 255)
    video = models.FileField(upload_to="Meterials") 