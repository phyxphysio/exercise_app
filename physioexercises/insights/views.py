from django.shortcuts import render
from patient_activation.forms import LastAttendanceReportForm
from .insights_utils import process_data
from django.contrib.auth.decorators import login_required

@login_required
def produce_insights(request):
    if request.method == "POST":
        form = LastAttendanceReportForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            graph_div =  process_data(file)
            return render(request,'insights/insights.html', {'form':form,'graph_div':graph_div})
            

    form = LastAttendanceReportForm()
    return render(request,'insights/insights.html', {"form": form})
