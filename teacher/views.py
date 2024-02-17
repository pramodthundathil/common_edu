from django.shortcuts import render, redirect
from Home.models import Course, TeacherProfile, StudentProfile
from django.contrib import messages
from .models import Exam, Question, Result, Meterials, Videostudylink
from .forms import QuestionCreationForm, MetirialAddForm, VideoAddForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime


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
    exams = Exam.objects.filter(teacher = TeacherProfile.objects.get(user = request.user))
    if request.method == "POST":
        exam  = request.POST["exam"]
        data = Exam.objects.create(exam_name = exam,question_number = 0, total_marks = 0,  teacher = TeacherProfile.objects.get(user = request.user))
        data.save()
        messages.info(request,"Data Saved...")
        return redirect("HostExam")
    
    context = {
        "exams":exams
    }
    return render(request,"teacherhostexam.html",context)

def Examexperyupdate(request,pk):
    exam = Exam.objects.get(id = pk)
    if request.method == "POST":
        date = request.POST["date"]
        exam.expery = date
        exam.save()
        messages.info(request,"Data Saved...")
        return redirect("HostExam")
    return redirect("HostExam")

def AddQuestionstoexam(request,pk):
    exam  = Exam.objects.get(id = pk)
    form = QuestionCreationForm()
    question = Question.objects.filter(course = exam)

    if request.method == "POST":
        form = QuestionCreationForm(request.POST)
        if form.is_valid():
            question = form.save()
            question.course = exam
            question.save()
            exam.question_number += 1
            exam.total_marks += question.marks
            exam.save()
            messages.info(request,"Data Deleted...")
            return redirect("AddQuestionstoexam", pk = pk)
        
    context = {
        "form":form,
        "exam":exam,
        "question":question
    }

    return render(request,"TeacherAddExam.html",context)


def DeleteQuestion(request,pk):
    question = Question.objects.get(id = pk)
    exam = question.course
    exam.question_number -= 1
    exam.total_marks -= question.marks
    exam.save()
    question.delete()
    messages.info(request,"Question Deleted....")
    return redirect("AddQuestionstoexam",pk = exam.id)


def DeleteExam(request,pk):
    Exam.objects.get(id=pk).delete()
    messages.info(request,"Data Deleted...")
    return redirect("HostExam")


def TeacherStudentView(request):
    teacher = TeacherProfile.objects.get(user = request.user)
    student = StudentProfile.objects.filter(course = teacher.course)

    context = {
        "student":student
    }
    return render(request,"teacherstudent.html",context)



def TeacherProfiles(request):
    return render(request,"teacherprofile.html")

def StudentsMark(request):
    return render(request,"teacherstudentmark.html")


def StudentExams(request):
    student = StudentProfile.objects.get(user = request.user )
    teacher = TeacherProfile.objects.get(course = student.course)
    exam = Exam.objects.filter(teacher = teacher, expery__gte = datetime.now() )

    context = {
        "exam":exam
    }
    return render(request,"studentexam.html",context)

def AttendtheExam(request,pk):
    exam = Exam.objects.get(id  = pk)
    if Result.objects.filter(student = StudentProfile.objects.get(user = request.user),exam = exam ).exists():
        text = ''''
        <h1 style='color:blue;text-align:center'>
        You Already attended this exam please go to
        <a href="/teacher/StudentExams" style='padding:10px 20px;border-radius:10px;background-color:red;color:white'>Exam Home</a>
        </h1>
        '''
        return HttpResponse(text)

    context = {
        "exam":exam
    }
    return render(request,"examattenstart.html",context)

def EneterExamination(request,pk):
    exam = Exam.objects.get(id = pk)
    questions = Question.objects.filter(course = exam)


    context = {
        "exam": exam,
        "questions":questions
    }
    if request.method=='POST':
        pass
    response= render(request,"Examination.html",{'course':exam,'questions':questions})
    response.set_cookie('course_id',exam.id)
    return response

@csrf_exempt
def calculate_marks(request):
    if request.COOKIES.get('course_id') is not None:
        course_id = request.COOKIES.get('course_id')
        exam=Exam.objects.get(id=course_id)
        
        total_marks=0
        questions= Question.objects.all().filter(course=exam)
        for i in range(len(questions)):
            
            selected_ans = request.COOKIES.get(str(i+1))
            actual_answer = questions[i].answer
            if selected_ans == actual_answer:
                total_marks = total_marks + questions[i].marks
        student = StudentProfile.objects.get(user=request.user)
        result = Result.objects.create(student = student ,exam = exam,marks= total_marks)
        result.save()
        return redirect("ExamCompleted")
    return redirect("StudentExams")

def ExamCompleted(request):
    return render(request,"examcompleted.html")


def TeacherMarkView(request,pk):
    student = StudentProfile.objects.get(id = pk)
    marks = Result.objects.filter(student = student )

    context = {
        "mark":marks,
        "student":student
    }
    return render(request,"teachermarkview.html",context)

def ApproveMark(request,pk):
    res = Result.objects.get(id = pk)
    res.approval = True
    res.save()
    messages.info(request,"Mark Approved....")
    
    return redirect("TeacherStudentView")

def StudentMarkView(request):
    student = StudentProfile.objects.get(user  = request.user)
    mark = Result.objects.filter(student = student, approval = True)
    context = {
        "mark":mark
    }
    return render(request,"studentmarkview.html",context)


def StudentmarksAdmin(request):
    mark = Result.objects.all()

    context = {
        "mark":mark
    }
    return render(request,"adminmarkview.html",context)

def ApproveMarkAdmin(request,pk):
    res = Result.objects.get(id = pk)
    res.approval = True
    res.save()
    messages.info(request,"Mark Approved....")
    return redirect("StudentmarksAdmin")

def Deletemark(request,pk):
    res = Result.objects.get(id = pk)
    res.delete()
    messages.info(request,"Mark Deleted....")
    return redirect("StudentmarksAdmin")
    

def Studymaterials(request):
    form = MetirialAddForm()
    form1 = VideoAddForm()
    materials = Meterials.objects.all()
    videos = Videostudylink.objects.all()

    if request.method == "POST":
        form = MetirialAddForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.save()
            data.teacher = TeacherProfile.objects.get(user = request.user)
            data.save()
            messages.info(request,"Data Saved....")
            return redirect("Studymaterials")

        else:
            messages.info(request,"Not done....")
            return redirect("Studymaterials")

    context = {
        "form":form,
        "form1":form1,
        "materials":materials,
        "videos":videos
    }
    return render(request,"studymeterials.html",context)

def VideoSave(request):
    if request.method == "POST":
        form = VideoAddForm(request.POST,request.FILES)
        if form.is_valid():
            data = form.save()
            data.teacher = TeacherProfile.objects.get(user = request.user)
            data.save()
            messages.info(request,"Data Saved....")
            return redirect("Studymaterials")
        else:
            messages.info(request,"Not done....")
            return redirect("Studymaterials")
    return redirect("Studymaterials")
    

    
def DeleteMeterial(request,pk):
    m = Meterials.objects.get(id = pk)
    m.Banner_image.delete()
    m.Metirial.delete()
    m.delete()
    messages.info(request,"Data deleted....")
    return redirect("Studymaterials")

def DeleteVideo(request,pk):
    m = Videostudylink.objects.get(id = pk)
    m.video.delete()
    m.delete()
    messages.info(request,"Data deleted....")
    return redirect("Studymaterials")

def StudentStudy(request):
    material = Meterials.objects.all()
    video = Videostudylink.objects.all()

    context = {
        "material":material,
        "video":video
    }
    return render(request,"matirial.html",context)
