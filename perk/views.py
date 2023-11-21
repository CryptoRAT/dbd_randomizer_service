from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PerkSerializer
from .models import Perk

# Create your views here.

class PerkView(viewsets.ModelViewSet):
    serializer_class = PerkSerializer
    queryset = Perk.objects.all()