from .models import Project

def getProject(id):
    return Project.objects.get(project_id=id)