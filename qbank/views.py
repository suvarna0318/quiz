from django.shortcuts import render,redirect
from .models import Question
from .forms import CreateQuestionForm,CreateAnswerForm
from django.contrib import messages

# Create your views here.
def home(request):
	return render(request,'qbank/home.html')

def questions(request):
	ans=""
	if request.method == "POST":
		ans=request.POST.get('choice')
		que=Question.objects.all()

	else:
		que=Question.objects.all()
	context={'objects':que,'ans':ans}
	# # print(context)
	return render(request,'qbank/question.html',context)

def createQuestion(request):

	if request.method == "POST":
		form=CreateQuestionForm(request.POST)
		# que=form.cleaned_data.get('question_text')
		# print(que)
		if form.is_valid():
			form.save()
			messages.success(request, ('Your Question was successfully added!'))
		else:
			messages.error(request, 'Error saving form')
		
	form=CreateQuestionForm()
	context={'form':form,
	}
	
	return render(request,'qbank/create_question.html',context)

def createAnswer(request):
	print("1")
	if request.method == "POST":
		form=CreateAnswerForm(request.POST)
		
		if form.is_valid():
			print("im in form")

			form.save()
			messages.success(request, ('Your Question was successfully added!'))
		else:
			messages.error(request, 'Error saving form')
		
	form=CreateAnswerForm()
	context={'form':form,
	}
	
	return render(request,'qbank/create_ans.html',context)

