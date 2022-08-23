from django.shortcuts import render
from django.views.generic.base import View
from .models import QuestionData
from .forms import QuestionForm
from django.http import HttpResponseRedirect
from django.urls import reverse


class firstquestionview(View):
    def get(self, request, *args, **kwargs):
        return render(request, "html/question1.html")

    def post(self,request, *args, **kwargs):
        try:
            question_form = QuestionForm(data=request.POST)
            if question_form.is_valid():
                obj = question_form.save()
                que_obj = QuestionData.objects.last()
                que_obj.question = "What is your total income per year?"  # question has beed settled static for now.
                que_obj.save()
                return HttpResponseRedirect(reverse('second-question'))

        except Exception as e:
            print("exception", e)
            print("ERROR : Form is invalid")
            print(question_form.errors)


class secondquestionview(View):
    def get(self, request, *args, **kwargs):
        return render(request, "html/question2.html")

    def post(self,request, *args, **kwargs):
        try:
            question_form = QuestionForm(data=request.POST)
            if question_form.is_valid():
                obj = question_form.save()
                que_obj = QuestionData.objects.last()
                que_obj.question = "How much is your house worth?"  # question has beed settled static for now.
                que_obj.save()
                return HttpResponseRedirect(reverse('third-question'))

        except Exception as e:
            print("exception", e)
            print("ERROR : Form is invalid")
            print(question_form.errors)


class thirdquestionview(View):
    def get(self, request, *args, **kwargs):
        return render(request, "html/question3.html")

    def post(self,request, *args, **kwargs):
        try:
            question_form = QuestionForm(data=request.POST)
            if question_form.is_valid():
                obj = question_form.save()
                que_obj = QuestionData.objects.last()
                que_obj.question = "How much money you are investing per year?"  # question has beed settled static for now.
                que_obj.save()
                return HttpResponseRedirect(reverse('success'))

        except Exception as e:
            print("exception", e)
            print("ERROR : Form is invalid")
            print(question_form.errors)

class successview(View):
    def get(self, request, *args, **kwargs):
        return render(request, "html/success.html")
