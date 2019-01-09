from django.db import models
from django.contrib.auth.models import User

# Create your models here.

widget_choices = (
    ('BT', 'Button'),
)

class Project(models.Model):
    name = models.CharField(max_length = 40)
    project_id = models.CharField(max_length = 40, primary_key=True)
    secret_key = models.CharField(max_length = 40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file_path = models.CharField(max_length = 200,default="NA")
    viewers = models.IntegerField(default = 0)

    class Meta:
        unique_together = ("name","project_id")