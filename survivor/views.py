from django.shortcuts import render
from rest_framework import viewsets

from .serializers import SurvivorSerializer
from .models import Survivor

# Create your views here.

class SurvivorView(viewsets.ModelViewSet):
    serializer_class = SurvivorSerializer
    queryset = Survivor.objects.all()