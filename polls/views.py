from django.shortcuts import render,HttpResponse

from polls.models import Project

# Create your views here.

def home(request):

    projects = Project.objects.all()

    return render(request, 'index.html',{'projects': projects})
