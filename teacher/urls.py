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
        path("DeleteExam/<int:pk>",views.DeleteExam,name="DeleteExam"),
        path("AddQuestionstoexam/<int:pk>",views.AddQuestionstoexam,name="AddQuestionstoexam"),
        path("DeleteQuestion/<int:pk>",views.DeleteQuestion,name="DeleteQuestion"),
        path("StudentExams",views.StudentExams,name="StudentExams"),
        path("Examexperyupdate/<int:pk>",views.Examexperyupdate,name="Examexperyupdate"),
        path("AttendtheExam/<int:pk>",views.AttendtheExam,name="AttendtheExam"),
        path("EneterExamination/<int:pk>",views.EneterExamination,name="EneterExamination"),
        path("calculate_marks",views.calculate_marks,name="calculate_marks"),
        path("ExamCompleted",views.ExamCompleted,name="ExamCompleted"),
        path("TeacherMarkView/<int:pk>",views.TeacherMarkView,name="TeacherMarkView"),
        path("StudentMarkView",views.StudentMarkView,name="StudentMarkView"),
        path("StudentmarksAdmin",views.StudentmarksAdmin,name="StudentmarksAdmin"),
        path("ApproveMark/<int:pk>",views.ApproveMark,name="ApproveMark"),
        path("ApproveMarkAdmin/<int:pk>",views.ApproveMarkAdmin,name="ApproveMarkAdmin"),
        path("Deletemark/<int:pk>",views.Deletemark,name="Deletemark"),
        path("Studymaterials",views.Studymaterials,name="Studymaterials"),
        path("VideoSave",views.VideoSave,name="VideoSave"),
        path("DeleteMeterial/<int:pk>",views.DeleteMeterial,name="DeleteMeterial"),
        path("DeleteVideo/<int:pk>",views.DeleteVideo,name="DeleteVideo"),
        path("StudentStudy",views.StudentStudy,name="StudentStudy"),
 

]     