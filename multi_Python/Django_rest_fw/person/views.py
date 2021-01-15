from django.shortcuts import render
from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerialize
# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerialize