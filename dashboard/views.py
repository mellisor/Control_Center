from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import Project
import string
import random
from uuid import uuid4

# Create your views here.

# TODO: Implement login
@login_required
def dashboard(request):
    if request.method == "POST":
        return create_project(request)
    projects = Project.objects.filter(user=request.user)
    return render(request,'dashboard.html', context = {"projects" : projects})

def create_project(request):
    exists = True
    while exists:
        pid = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(20))
        if len(Project.objects.filter(project_id=pid)) == 0:
            exists = False
    sid = str(uuid4())
    proj_name = request.POST.get('project_name')
    p = Project(name=proj_name,project_id=pid,secret_key=sid,user=request.user,file_path='Hi')
    p.save()
    open('projects/' + pid + '.html', 'w+')
    return redirect('/dashboard/edit/' + pid)

@login_required
def edit_project(request,slug):
    if len(Project.objects.filter(project_id=slug)) == 0:
        return HttpResponse("Doesn't Exist")
    content = open('projects/' + slug + '.html').read()
    return render(request,'project.html',context={'project':slug+'.html','content':content})
    