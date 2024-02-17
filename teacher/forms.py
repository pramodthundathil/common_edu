from django.forms import ModelForm
from .models import Question, Meterials, Videostudylink

class QuestionCreationForm(ModelForm):
    class Meta:
        model = Question
        fields = ["marks","question","option1","option2","option3","option4","answer"]

class MetirialAddForm(ModelForm):
     class Meta:
        model = Meterials
        fields = ["Title","description","Banner_image","Metirial"]

class VideoAddForm(ModelForm):
     class Meta:
        model = Videostudylink
        fields = ["Title","description","video"]

