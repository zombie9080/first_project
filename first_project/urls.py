"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from first_app.views import *
from django.views.generic import TemplateView
#from first_app.models import *
#from django.views.generic.list import ListView

#booklist = {
#    'queryset': Book.objects.all(),        
#    'template_name':   'listview.html', 
#}


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^firstapp/',include('first_app.urls')),
]
urlpatterns += patterns('',
    (r'^now/(?P<timezone>\d|10|11|12)/$',current_time),
    (r'^HELLO/(\w+)/$',HELLO),
    (r'^hello1/$',hello,{'template_name': 'hello1.html'}),
    (r'^hello2/$',hello,{'template_name': 'hello2.html'}),
    (r'^hello3/$',hello_nest(hello3)),
    (r'^hello4/$',hello_nest(hello4)),
    (r'^genericview/$',TemplateView.as_view(template_name='genericview.html')),
    #(r'^listview/$',ListView.as_view(**booklist)),
    (r'^listview/$',BookListView.as_view()),
)
