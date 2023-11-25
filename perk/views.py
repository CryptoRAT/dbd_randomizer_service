from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PerkSerializer
from .models import Perk


class PerkView(viewsets.ModelViewSet):
    serializer_class = PerkSerializer
    queryset = Perk.objects.all()


class SurvivorPerkView(viewsets.ModelViewSet):
    serializer_class = PerkSerializer
    queryset = Perk.objects.filter(type="Survivor")


class KillerPerkView(viewsets.ModelViewSet):
    serializer_class = PerkSerializer
    queryset = Perk.objects.filter(type="Killer")


class RandomSurvivorPerkView(viewsets.ModelViewSet):
    serializer_class = PerkSerializer
    queryset = Perk.objects.filter(type="Survivor").order_by('?')[:4]


class RandomKillerPerkView(viewsets.ModelViewSet):
    serializer_class = PerkSerializer
    queryset = Perk.objects.filter(type="Killer").order_by('?')[:4]