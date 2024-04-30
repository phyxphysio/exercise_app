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
            file = request.FILES["file"]
            result = process_report(file, user.username)
            return render(request, "patient_activation/patient_activation_success.html", {"email_count": result})
    else:
        form = LastAttendanceReportForm()
    return render(request, "patient_activation/patient_activation.html", {"form": form})


def process_report(f, sender):
    addresses = get_addresses(f)
    send_patient_activation(addresses=addresses, sender=sender)
