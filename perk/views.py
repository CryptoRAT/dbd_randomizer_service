from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import PerkSerializer
from .models import Perk


class PerkView(viewsets.ModelViewSet):
    serializer_class = PerkSerializer
    queryset = Perk.objects.all()

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        owner = request.data.get('owner')
        type = request.data.get('type')
        image_path = request.data.get('image_path')

        if not name or not owner or not type or not image_path:
            return Response({'error': 'Name, owner, type, and image_path are required'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data={'name': name, 'owner': owner, 'type': type, 'image_path': image_path})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        perk = self.get_object()
        perk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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