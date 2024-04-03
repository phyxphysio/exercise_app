from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field


class SearchForm(forms.Form):
    patient_email = forms.EmailField(required=False)
    patient_name = forms.CharField(initial="there", max_length=20, required=False)
    frequency = forms.CharField(
        initial="3-4 times per week", max_length=50, required=False
    )
    sets = forms.IntegerField(initial=2, required=False)
    reps = forms.IntegerField(initial=8, required=False)
    next_appointment = forms.CharField(initial='our next appointment', max_length=20, required=False)

    query = forms.CharField(label="Exercise keywords, separated by comma")


class EmailForm(forms.Form):
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
    recipient_list = forms.CharField()  # In real scenario, use EmailField and proper validation

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('subject' ),
            Field('message', rows=15, columns=40 ),
            Field('recipient_list'),
            Submit('submit', 'Send Email', css_class='btn btn primary my-4 mx-auto d-block w-50')
        )
