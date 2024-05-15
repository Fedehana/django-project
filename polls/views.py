from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
# Create your views here.
def index(request):
    questions = Question.objects.order_by("-date")

    context = {
        "questions": questions                      #pasos para guardar
    }
    return render(request, "index.html", context)

    # response = ''
    # for question in questions:
    #     response += f'{question.question_text}, '

    # return HttpResponse(response)

def detail(request, question_id):
    return HttpResponse("This is questions number: " + str(question_id))



