from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Project

# Create your views here.

# TODO: Implement login
@login_required
def dashboard(request):
    projects = Project.objects.filter(user=request.user)
    return render(request,'dashboard.html', context = {"projects" : projects})
