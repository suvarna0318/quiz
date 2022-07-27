from django import forms 
from .models import Answer,Question

class CreateQuestionForm(forms.ModelForm):
	print("working")
	class Meta:
		model=Question
		fields='__all__'

class CreateAnswerForm(forms.ModelForm):
	print("working")
	class Meta:
		model=Answer
		fields='__all__'