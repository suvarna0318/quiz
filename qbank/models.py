from django.db import models


class student(models.Model):
	name=models.CharField(max_length=10)

#Create your models here.
class Category(models.Model):
	cateory_name=models.CharField(max_length=250, unique=True)
	description=models.TextField(max_length=250)
	is_active= models.BooleanField(default='False')
	#sequence=
	def __str__(self):
		return self.cateory_name


class Question(models.Model):
	question_text=models.CharField(max_length=50, unique=True)
	score= models.IntegerField(default=0)
	#negative_score=
	#data_type=
	is_active= models.BooleanField(default='False')
	category= models.ForeignKey(Category, on_delete=models.CASCADE)
	#sequence=
	def __str__(self):
		return self.question_text

class Answer(models.Model):
	question_text= models.ForeignKey(Question, on_delete=models.CASCADE)
	choice1 = models.CharField(max_length=50, unique=True)
	choice2 = models.CharField(max_length=50, unique=True)
	choice3 = models.CharField(max_length=50, unique=True)
	choice4 = models.CharField(max_length=50, unique=True)
	answer_key=models.IntegerField()
	answer_value=models.CharField(max_length=50, unique=True)#correct_answer 
	is_active=models.BooleanField(default='False')
	score=models.IntegerField(default=0)
	negative_score=models.IntegerField(default=0)
	sequence=models.IntegerField(default=0)
	is_correct_answer=models.BooleanField(default='False')
	def __str__(self):
		return self.question_text

