from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question,Choice
from django.db.models import F
from django.urls import reverse
from django.views import generic
# Create your views here.
def detail(request,question_id):
    # return HttpResponse("You are looking at question %s." % question_id)
    # try:
    #     question=Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("The question does not exist")
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/detail.html",{'question':question})

def results(request,question_id):
    # response="You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question=get_object_or_404(Question,pk=question_id)
    return render(request,"polls/results.html",{'question':question})

def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question=get_object_or_404(Question,pk=question_id)
    try:
        selected_choice=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,"polls/detail.html",{'question':question,'error_message':'You did not select a choice',},)
    else:
        selected_choice.votes=F('votes')+1
        selected_choice.save()
        
        return HttpResponseRedirect(reverse('results',args=(question_id,)))
    
def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')[:5]
    context={'latest_question_list':latest_question_list}
    return render(request,'polls/index.html',context)

class IndexView(generic.ListView):
    template_name='polls/index.html'
    context_object_name='latest_question_list'
    
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model=Question
    template_name="polls/detail.html"
    
class ResultView(generic.DetailView):
    model=Question
    template_name="polls/results.html"
    
