from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from . models import Quiz, User, Complited


def index(request):
    return render(request,'quizes/index.html')

def list(request):
    quizes_list = Quiz.objects.order_by('id')
    return render(request, 'quizes/list.html', {'quizes_list': quizes_list})

def detail(request, quiz_id):
    try:
        a = Quiz.objects.get( id = quiz_id)
    except:
        raise Http404("Опрос не найден")

    questions_list = a.question_set.all()

    return render(request, 'quizes/detail.html', {'quiz': a, 'questions_list':questions_list})

def current_user(request):
    a = User.objects.all()
    a.create(user_name = request.POST['name'])
   
    return HttpResponseRedirect( reverse('quizes:list'))

def complited_question(request):
    b = Complited.objects.all()
    b.create()
    