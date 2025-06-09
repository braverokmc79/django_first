from django import forms
from .models import Question, Choice

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']
        widgets = {
            'question_text': forms.TextInput(attrs={'class': 'form-control input-h3'}),
            'pub_date': forms.DateTimeInput(attrs={
                'class': 'form-control input-h3', 
                'type': 'datetime-local'
            }),
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']
        
        
        
        
        