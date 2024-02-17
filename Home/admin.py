from django.contrib import admin
from .models import *
from careers.models import *

# Register your models here.
admin.site.register(RecruiterData)
admin.site.register(Joblist)
admin.site.register(Course)
admin.site.register(Education)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(ResumeWritingTips)
admin.site.register(Jobapplication)
admin.site.register(InterViewSchedule)

