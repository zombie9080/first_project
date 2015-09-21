
# -*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime,timedelta
from django.views.generic.list import ListView
from .models import *
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from .form import Userform, Fileform

# Create your views here.

class BookListView(ListView):
    template_name = 'listview.html'
    model = Book
    #queryset = Book.objects.filter(title__icontains='django')
    if cache.get('book'):
        queryset = cache.get('book')
    else:
    	queryset = Book.objects.filter(title__icontains='django')
    	cache.set('book',queryset)
    def get_context_data(self,**kwargs):
    	context = super(BookListView,self).get_context_data(**kwargs)
    	return context

@cache_page(60*2)
def cachepages(request):
	pub = Publisher.objects.all()
	return render_to_response('cachepage.html',{'publishers':pub})
	
<<<<<<< HEAD
def index(req):
	hint = ''
	if req.method == 'POST':
		ff = Fileform(req.POST,req.FILES)
		if ff.is_valid():
			hint = 'upload success'
			print ff.cleaned_data['file'].name
			print ff.cleaned_data['file'].size
			fp = file('upload/'+ff.cleaned_data['file'].name,'wb')
			s = ff.cleaned_data['file'].read()
			fp.write(s)
			fp.close()
	username = req.COOKIES.get('username','')
	FF = Fileform()
	return render_to_response('index.html',{'ff':FF,'value':'hello','mima':'123456','username':username,'hint':hint})
=======


def index(request):
    return render_to_response('index.html',{'value':'hello','mima':'123456'})
>>>>>>> 4c5505470601dd2469a5ef398dab2ece9f85232c

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


def login(req):
	if req.method == 'POST':
		uf = Userform(req.POST)
		if uf.is_valid():	# 不可少
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			users = User.objects.filter(username__exact=username,password__exact=password)
			if users:
				response = HttpResponseRedirect('/firstapp/index/')
				response.set_cookie('username', username, 3600)
				return response
			else:
				uf = Userform()
				return render_to_response('login.html',{'uf':uf,'hint':'wrong username or secrete'})
	else:
		uf = Userform()
	return render_to_response('login.html',{'uf':uf})

def register(req):
	if req.method == 'POST':
		uf = Userform(req.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			users = User.objects.filter(username__exact=username)
			if users:
				uf = Userform()
				render_to_response('register.html',{'uf':uf,'hint':'username exist'})	
			else:
				user = User(username=username,password=password)
				user.save()
				return HttpResponseRedirect('/firstapp/index/')
	else:
		uf = Userform()
	return render_to_response('register.html',{'uf':uf})
