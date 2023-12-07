from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .serializers import SurvivorSerializer
from .models import Survivor


class SurvivorView(viewsets.ModelViewSet):
    parser_classes = [JSONParser]
    serializer_class = SurvivorSerializer
    queryset = Survivor.objects.all()

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        image_path = request.data.get('image_path')

        if not name or not image_path:
            return Response({'error': 'Name and image_path are required'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data={'name': name, 'image_path': image_path})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        name = request.data.get('name')
        image_path = request.data.get('image_path')

        if not name or not image_path:
            return Response({'error': 'Name and image_path are required'}, status=status.HTTP_400_BAD_REQUEST)

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)

    def destroy(self, request, *args, **kwargs):
        survivor = self.get_object()
        survivor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RandomSurvivorView(viewsets.ModelViewSet):

    def random(self, request, *args, **kwargs):
        if request.method == 'POST':
            # Handle POST logic here
            survivor = Survivor.objects.order_by('?').first()
            serializer = SurvivorSerializer(survivor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Handle GET logic here
            print("GET request successful")

