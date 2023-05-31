from django import forms
from .models import QuizCategory, Question, Answer

class QuizCategoryForm(forms.ModelForm):
    class Meta:
        model = QuizCategory
        fields = ('name', 'description')
       

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ()
    
