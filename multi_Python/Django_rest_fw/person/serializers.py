from .models import Person
from rest_framework import serializers

class PersonSerialize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'age')
