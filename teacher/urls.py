from django.urls import path 
from .import views  

urlpatterns = [
    
        path("AddNewCourse",views.AddNewCourse,name="AddNewCourse"),
        path("Coursedelete/<int:pk>",views.Coursedelete,name="Coursedelete"),
        path("ApproveStudent/<int:pk>",views.ApproveStudent,name="ApproveStudent"),
        path("ApproveTeacher/<int:pk>",views.ApproveTeacher,name="ApproveTeacher"),
        path("HostExam",views.HostExam,name="HostExam"),
        path("TeacherProfiles",views.TeacherProfiles,name="TeacherProfiles"),
        path("TeacherStudentView",views.TeacherStudentView,name="TeacherStudentView"),
        path("StudentsMark",views.StudentsMark,name="StudentsMark"),

        
]    