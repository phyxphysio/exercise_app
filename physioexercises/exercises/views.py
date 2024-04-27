from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic import ListView, TemplateView
from .models import Exercise
from .forms import SearchForm, EmailForm
from django.conf import settings


from django.core.mail import send_mail


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
                if exercise := Exercise.objects.filter(
                    name__icontains=term.strip(" ")
                ).first():
                    exercises.append(exercise)
                else:
                    form.add_error("query", f'No matches for "{term}"')
            if not form.errors:
                # Assuming 'exercises' is a queryset that might be empty
                exercise_ids = [exercise.id for exercise in exercises if exercise]

                # Store session data
                request.session["message"] = {
                    "exercises": exercise_ids,
                    "sets": sets,
                    "reps": reps,
                    "frequency": frequency,
                    "patient_name": patient_name,
                    "next_appointment": next_appointment,
                    "patient_email": form.cleaned_data.get("patient_email"),
                }

                # Redirect to the email sending function
                return redirect("send_email")

    else:
        form = SearchForm()
    return render(request, "exercises/search_form.html", {"form": form})


def send_email(request):
    message_data = request.session.get("message")
    if not message_data:
        return redirect("home")  # Redirect if session data is missing

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")

        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            recipient_list = form.cleaned_data["recipient_list"]  # Adjust as needed

            # Send the email
            send_mail(
                subject=subject,
                message=message,  # Plain text version
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[recipient_list],
            )

            return redirect("success")
    else:
        form = email_form(message_data)
    return render(request, "exercises/email_preview.html", {"form": form})


def email_form(message_data):
    # Prepare initial data for the form
    patient_name = message_data["patient_name"]  # The name of the patient
    frequency = message_data[
        "frequency"
    ]  # The frequency of the specific action/medication
    sets = message_data[
        "sets"
    ]  # The number of sets (often in the context of physical exercises or any other routine)
    reps = message_data["reps"]  # The number of repetitions in every set
    next_appointment = message_data[
        "next_appointment"
    ]  # The next scheduled appointment date (can be a date string or a datetime object)
    exercises_list = [
        Exercise.objects.get(id=ex_id) for ex_id in message_data["exercises"]
    ]

    message = f"""Hi {patient_name},
Here are the exercises we discussed today. 
Try do these {frequency} times per week.
         """
    for exercise in exercises_list:
        message += (
            f"\n{exercise.name} - {exercise.link}\n-{sets} sets of {reps} repetitions\n"
        )
    message += f"\nSee you at {next_appointment},\n\n Liam\nPhysioward Brookvale "

    initial_data = {
        "subject": "Physio Exercises",
        "message": message,
        "recipient_list": message_data["patient_email"].strip(
            "'"
        ),  # Adjust based on your requirements
    }
    return EmailForm(initial=initial_data)


class SuccessView(TemplateView):
    template_name = "exercises/success.html"


class ExerciseListView(ListView):
    model = Exercise
    template = "exercises/exercises.html"
