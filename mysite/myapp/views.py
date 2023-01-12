from django.shortcuts import render
from rest_framework import viewsets

from .serializer import PersonSerializer, TriageSerializer
from .models import Person, Triage
from .templates.forms import PersonForm, TriageForm


# creating views
# function to view the home page
def home_view(request):
    return render(request, "home.html")


# function to view the triage
def triage_view(request):
    context = {'form': TriageForm()}
    return render(request, "triage.html", context)


# function to view the registration
def reg_view(request):
    context = {'form': PersonForm()}
    return render(request, "registration.html", context)


# create a view set
class PersonViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Person.objects.all()
    # specify serializer to be used
    serializer_class = PersonSerializer


# create a view set
class TriageViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Triage.objects.all()
    # specify serializer to be used
    serializer_class = TriageSerializer

