from django.shortcuts import render
from patient_activation.forms import LastAttendanceReportForm
from .insights_utils import process_data

def produce_insights(request):
    if request.method == "POST":
        form = LastAttendanceReportForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            path =  process_data(file)
            render(request,'insights/insights.html', {"form": form, 'path':path})
            

    form = LastAttendanceReportForm()
    return render(request,'insights/insights.html', {"form": form})
