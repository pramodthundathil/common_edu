from django.shortcuts import render, redirect
from Home.models import Course, TeacherProfile, StudentProfile
from django.contrib import messages

# Create your views here.

def AddNewCourse(request):
    if request.method == "POST":
        course = request.POST['course']
        course1 = Course.objects.create(course = course)
        course1.save()
        messages.info(request,"Course Added")
        return redirect("AdminIndex")
    return redirect("AdminIndex")

def Coursedelete(request,pk):
    Course.objects.get(id= pk).delete()
    messages.info(request,"Course deleted")
    return redirect("AdminIndex")


def ApproveTeacher(request,pk):
    teacher = TeacherProfile.objects.get(id = pk)
    course = Course.objects.all()
    if request.method == "POST":
        cour = request.POST['course']
        teacher.course = Course.objects.get(id = int(cour))
        teacher.approval_status = True
        teacher.save()
        messages.info(request,"Teacher Approved Success")
        return redirect("AdminIndex")
    context = {
        "teacher":teacher,
        "course":course

    }
    return render(request,"approveteacher.html",context)

def ApproveStudent(request,pk):
    teacher = StudentProfile.objects.get(id = pk)
    course = Course.objects.all()
    if request.method == "POST":
        cour = request.POST['course']
        teacher.course = Course.objects.get(id = int(cour))
        teacher.approval_status = True
        teacher.save()
        messages.info(request,"Student Approved Success")
        return redirect("AdminIndex")
    
    context = {
        "teacher":teacher,
        "course":course

    }
    return render(request,"approvestudent.html",context)


def HostExam(request):
    return render(request,"teacherhostexam.html")

def TeacherStudentView(request):
    return render(request,"teacherstudent.html")



def TeacherProfiles(request):
    return render(request,"teacherprofile.html")

def StudentsMark(request):
    return render(request,"teacherstudentmark.html")