from django.shortcuts import render
from django.views.generic.base import View
from .models import QuestionData
from .forms import QuestionForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from textwrap import wrap


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
        que_obj = QuestionData.objects.all().order_by('-id')
        buffer = io.BytesIO()
        p = canvas.Canvas(buffer,pagesize=A4)
        t = p.beginText()
        t.setFont('Helvetica-Bold', 10)
        t.setCharSpace(2)
        t.setTextOrigin(30, 800)
        income_value = str(que_obj[2].value) + " " + que_obj[2].currency
        home_value = str(que_obj[1].value) + " " + que_obj[1].currency
        invest_value = str(que_obj[0].value) + " " + que_obj[0].currency
        text = "(1) What is your total income per year?" + "-" + income_value + "   (2) How much is your house worth?" + "-" + home_value +"   (3) How much money you are investing per year?" + "-" + invest_value
        wraped_text = "\n".join(wrap(text, 80)) # 80 is line width
        t.textLines(wraped_text)

        p.drawText(t)
        p.showPage()
        p.save()

        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='docassemble.pdf')
