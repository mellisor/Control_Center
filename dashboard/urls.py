from django.contrib import admin
from django.urls import path, include

from . import views

app_name = "dashboard"

urlpatterns = [
    path('', views.dashboard, name="index"),
    path('edit/<slug:slug>', views.edit_project, name="edit"),
    path('open/<slug:slug>', views.view_project, name="view"),
]
