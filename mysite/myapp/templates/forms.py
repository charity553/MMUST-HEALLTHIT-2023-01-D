from django import forms


# creating a form for registration model
class PersonForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    area_name = forms.CharField(max_length=50)
    age = forms.CharField(max_length=10)


# creating a form for triage model
class TriageForm(forms.Form):
    temperature = forms.CharField(max_length=3)
    blood_pressure = forms.CharField(max_length=3)
    respiratory_rate = forms.CharField(max_length=3)
    pulse_rate = forms.CharField(max_length=10)
    weight = forms.CharField(max_length=3)
    height = forms.CharField(max_length=3)

