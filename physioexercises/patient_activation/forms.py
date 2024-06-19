from django import forms 

class LastAttendanceReportForm(forms.Form):
    service = forms.ChoiceField(choices={
        'physiotherapy': 'Physiotherapy',
        'hydrotherapy': 'Hydrotherapy'
    }, label="Select a Service Type")
 
    report = forms.FileField()
