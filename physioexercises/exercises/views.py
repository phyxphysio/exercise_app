from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, FormView
from .models import Exercise
from .forms import SearchForm


class ExerciseListView(ListView):
    model = Exercise
    template_name = "exercises/home.html"
    context_object_name = "exercises"


def search_exercises(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            patient_name = form.cleaned_data["patient_name"]
            frequency = form.cleaned_data["frequency"]
            sets = form.cleaned_data["sets"]
            reps = form.cleaned_data["reps"]
            next_appointment = form.cleaned_data["next_appointment"]

            search_terms = query.split(",")
            exercises = []
            for term in search_terms:
                exercises.append(Exercise.objects.filter(name__icontains=term.strip(' ')).first())
            # exercises = Exercise.objects.filter(name__icontains=query)
            return render(
                request,
                "exercises/search_results.html",
                {
                    "exercises": exercises,
                    "sets": sets,
                    "reps": reps,
                    "frequency": frequency,
                    "patient_name": patient_name,
                    "form": form,
                    "next_appointment": next_appointment,
                },
            )
    else:
        form = SearchForm()
    return render(request, "exercises/search_form.html", {"form": form})
