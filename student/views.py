from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User
# Create your views here.

from .models import Post, Stage, Event, Logement, Transport , User

def Home(request):
    template=loader.get_template('student/base.html')
    list=User.objects.all()
    return render(request,'student/base.html',{'list':list})
    # users =User.objects.all()
    # posts = Post.objects.all()
    # stages = Stage.objects.all()
    # events = Event.objects.all()
    # logements = Logement.objects.all()
    # transports = Transport.objects.all()
    # return render(request, 'student/base.html', {'user': users.get} )
    # return HttpResponse("Welcome to the home page!") 
    # return render(request, 'post_detail.html', {'post': posts.get} ) ,render(request,'stage_detail.html', {'stage': stages.get} ),render(request,'event_detail.html', {'event': events.get}) ,render(request, 'logement_detail.html', {'logement': logements.get}) ,render(request, 'transport_detail.html', {'transport': transports.get} )

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def stage_detail(request, pk):
    stage = Stage.objects.get(pk=pk)
    return render(request, 'stage_detail.html', {'stage': stage})

def event_detail(request, pk):
    event = Event.objects.get(pk=pk)
    return render(request, 'event_detail.html', {'event': event})

def logement_detail(request, pk):
    logement = Logement.objects.get(pk=pk)
    return render(request, 'logement_detail.html', {'logement': logement})

def transport_detail(request, pk):
    transport = Transport.objects.get(pk=pk)
    return render(request, 'transport_detail.html', {'transport': transport})