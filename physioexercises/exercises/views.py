from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from .models import Exercise

class ExerciseListView(ListView):
    model = Exercise
    template_name = 'exercises/home.html'
    context_object_name = 'exercises'
