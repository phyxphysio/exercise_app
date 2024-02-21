from django import forms


class SearchForm(forms.Form):
    patient_email = forms.EmailField(required=False)
    patient_name = forms.CharField(initial="there", max_length=20, required=False)
    frequency = forms.CharField(
        initial="3-4 times per week", max_length=50, required=False
    )
    sets = forms.IntegerField(initial=2, required=False)
    reps = forms.IntegerField(initial=8, required=False)
    next_appointment = forms.CharField(initial='our next appointment', max_length=20, required=False)

    query = forms.CharField(label="Exercise keywords, seperated by comma")


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    recipient_list = forms.CharField()  # In real scenario, use EmailField and proper validation
