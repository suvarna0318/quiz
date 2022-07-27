"""quizapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from qbank import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('all_questions/',views.all_questions,name='all_questions'),
    path('single_question/<int:pk>/',views.single_question,name='single_question'),
    path('delete_question/<int:id>/',views.delete_question,name='delete_question'),
    path('questions/',views.questions,name='questions'),
    path('createQuestion/',views.createQuestion,name='createQuestion'),
    path('createAnswer/',views.createAnswer,name='createAnswer'),

]
