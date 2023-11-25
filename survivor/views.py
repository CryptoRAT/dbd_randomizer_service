from django.shortcuts import render
from rest_framework import viewsets

from .serializers import SurvivorSerializer
from .models import Survivor


class SurvivorView(viewsets.ModelViewSet):
    serializer_class = SurvivorSerializer
    queryset = Survivor.objects.all()


class RandomSurvivorView(viewsets.ModelViewSet):
    serializer_class = SurvivorSerializer
    queryset = Survivor.objects.all().order_by('?')[:1]