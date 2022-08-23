from django import forms
from .models import QuestionData


class QuestionForm(forms.ModelForm):
    class Meta():
        model = QuestionData
        fields = ('currency','value')