from rest_framework import serializers
from .models import Person, Triage


# creating serializers for each table (Person and Triage)
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'area_name', 'age')


class TriageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Triage
        fields = ('temperature', 'blood_pressure', 'respiratory_rate', 'pulse_rate', 'weight', 'height')
