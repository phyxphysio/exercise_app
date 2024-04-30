from django import forms 

class LastAttendanceReportForm(forms.Form):
    file = forms.FileField()
