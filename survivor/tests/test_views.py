import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from survivor.models import Survivor

@pytest.mark.django_db
def test_survivor_create_valid():
    client = APIClient()
    url = reverse('survivor-list')  # Matches the new survivor-list route

    # Valid data for creation
    data = {
        'name': 'Dwight Fairfield',
        'image_path': '/path/to/dwight.jpg'
    }

    response = client.post(url, data, format='json')

    # Check that the survivor was created successfully
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'Dwight Fairfield'
    assert response.data['image_path'] == '/path/to/dwight.jpg'

@pytest.mark.django_db
def test_survivor_create_invalid():
    client = APIClient()
    url = reverse('survivor-list')  # Matches the survivor-list route

    # Invalid data (missing required fields)
    data = {'name': 'Dwight Fairfield'}

    response = client.post(url, data, format='json')

    # Check that the request fails due to missing fields
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'error' in response.data

@pytest.mark.django_db
def test_survivor_update_valid():
    client = APIClient()
    # Create a Survivor instance to update
    survivor = Survivor.objects.create(name='Dwight Fairfield', image_path='/path/to/dwight.jpg')
    url = reverse('survivor-detail', kwargs={'pk': survivor.pk})  # Matches survivor-detail

    # Valid update data
    update_data = {
        'name': 'Meg Thomas',
        'image_path': '/path/to/meg.jpg'
    }

    response = client.put(url, update_data, format='json')

    # Check that the update was successful
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Meg Thomas'
    assert response.data['image_path'] == '/path/to/meg.jpg'

@pytest.mark.django_db
def test_survivor_destroy():
    client = APIClient()
    # Create a Survivor instance to delete
    survivor = Survivor.objects.create(name='Dwight Fairfield', image_path='/path/to/dwight.jpg')
    url = reverse('survivor-detail', kwargs={'pk': survivor.pk})  # Matches survivor-detail

    # Send delete request
    response = client.delete(url)

    # Check that the delete was successful
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Survivor.objects.filter(pk=survivor.pk).count() == 0

@pytest.mark.django_db
def test_random_survivor_get():
    client = APIClient()
    url = reverse('random-survivor')  # Matches random-survivor route

    # Send GET request (though random survivor method only handles POST for now)
    response = client.get(url)

    # The GET request is only printing for now, check the print side-effect if necessary
    assert response.status_code == status.HTTP_200_OK
    # No actual return on GET, but it should not raise an error
