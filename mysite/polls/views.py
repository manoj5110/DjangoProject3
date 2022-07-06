from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question


def index(request):
    latest_question_list=Question.objects.order_by('pub_date')[:5]
    # template_name=loader.get_template('polls/index.html')
    context_name={'latest_question_list':latest_question_list}
    # output=','.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template_name.render(context_name,request))
    return render(request,'polls/index.html',context_name)

# Create your views here.
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)