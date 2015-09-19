from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from datetime import datetime,timedelta
from .models import *
from django.views.generic.list import ListView

# Create your views here.


def index(request):
    return render_to_response('index.html',{'value':'hello','mima':'123456'})

def BookListView(ListView):
    model = Book
    queryset = Book.objects.filter(title__icontains='python')
    template_name = 'listview.html'
    def get_context_data(self,**kwargs):
        context = super(BookListView,self).get_context_data(**kwargs)
        return context


def current_time(request,timezone):
    print(int(timezone))
    now = datetime.now()+timedelta(hours=int(timezone))
    print(now)
    return HttpResponse("current time: %s" % (now))	

def HELLO(request,arg):
    print(arg)
    return render_to_response('hello.html',{'name':arg})

def hello(request,template_name):
    return render_to_response(template_name)

def hello3(request):
    return render_to_response('hello3.html')
def hello4(request):
    return render_to_response('hello4.html')

def hello_nest(func):
    def hello_func(request):
        print(func.__name__)
        return func(request)
    return hello_func
