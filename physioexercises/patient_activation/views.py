# views.py
from django.shortcuts import render
from .forms import LastAttendanceReportForm
from django.contrib.auth.decorators import login_required
from .activation_utils import get_addresses, send_patient_activation


@login_required
def handle_report_upload(request):
    if request.method == "POST":
        form = LastAttendanceReportForm(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            file = request.FILES["report"]
            service = request.POST.get('service')
            email_count = process_report(file, user.username, service)
            return render(
                request,
                "patient_activation/patient_activation_success.html",
                {"email_count": email_count},
            )
    else:
        form = LastAttendanceReportForm()
    return render(request, "patient_activation/patient_activation.html", {"form": form})


def process_report(f, sender, service):
    return send_patient_activation(addresses=get_addresses(f, service), sender=sender, service=service)


def preview_activation_email(request):
    booking_link = "https://physioward.com.au/book-now/"
    image_url = "https://physioward.com.au/wp-content/uploads/2022/09/physioward-secondary-logo-stacked-left-full-color-rgb.svg"

    name = "Patient name"
    sender = "Physiotherapist Name"

    return render(
        template_name="patient_activation/preview_activation.html",
        context={
            "sender": sender,
            "booking_link": booking_link,
            "image_url": image_url,
            "name": name,
        },
        request=request
    )
