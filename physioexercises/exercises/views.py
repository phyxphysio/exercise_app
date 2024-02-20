from django.shortcuts import render, redirect

# Create your views here.

from django.views.generic import ListView, FormView, TemplateView
from .models import Exercise
from .forms import SearchForm, EmailForm
from django.conf import settings

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

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
                exercises.append(
                    Exercise.objects.filter(name__icontains=term.strip(" ")).first()
                )
            # exercises = Exercise.objects.filter(name__icontains=query)

            request.session["message"] = {
                "exercises": [exercise.id for exercise in exercises],
                "sets": sets,
                "reps": reps,
                "frequency": frequency,
                "patient_name": patient_name,
                "next_appointment": next_appointment,
                'patient_email': form.cleaned_data['patient_email']
            }
            return redirect("send_email")

    else:
        form = SearchForm()
    return render(request, "exercises/search_form.html", {"form": form})

# views.py

def send_email(request):
    message_data = request.session.get('message')
    if not message_data:
        return redirect('home')  # Redirect if session data is missing

    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_list = [form.cleaned_data['recipient_list']]  # Adjust as needed

            # Send the email
            send_mail(
                subject=subject,
                message=strip_tags(message),  # Plain text version
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=recipient_list,
                html_message=message,  # HTML version
            )

            return redirect('success')
    else:
        # Prepare initial data for the form
        exercises_list = [Exercise.objects.get(id=ex_id) for ex_id in message_data['exercises']]
        html_content = render_to_string("exercises/search_results.html", {"message_data": message_data, "exercises": exercises_list})
        initial_data = {
            'subject': "Physio Exercises",
            'message': html_content,
            'recipient_list': [message_data['patient_email']],  # Adjust based on your requirements
        }
        form = EmailForm(initial=initial_data)

    return render(request, "exercises/email_preview.html", {"form": form})




# def send_email(request):
#     if request.method == "POST":
#         # When the user approves the email content, send the email
#         message_data = request.session.get('message')
#         if message_data:
#             exercises_list = [Exercise.objects.get(id=ex_id) for ex_id in message_data['exercises']]

#             # Render your HTML content
#             html_content = render_to_string(
#                 "search_results.html", {"message_data": message_data, 'exercises':exercises_list}
#             )
#             plain_message = strip_tags(html_content)

#             send_mail(
#                 subject="Physio Exercises",
#                 message=plain_message,  # Plain text version
#                 from_email="liam.miller.pt@gmail.com",
#                 recipient_list=["20miller13@gmail.com"],
#                 html_message=html_content,  # HTML version
#             )

#             return redirect('success')  # Replace 'email_sent_success' with your success URL name
#     else:
#         message_data = request.session.get('message')
#         exercises_list = [Exercise.objects.get(id=ex_id) for ex_id in message_data['exercises']]

#         if not message_data:
#             return redirect('home')  # Fallback in case there's no data
        
#         # Render the preview template with the email message data
#         return render(request, "exercises/search_results.html", {"message_data": message_data, "exercises":exercises_list})

class SuccessView(TemplateView):
    template = 'exercises/success.html' 

