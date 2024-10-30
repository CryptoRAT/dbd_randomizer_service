import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from killer.models import Killer

@pytest.mark.django_db
def test_killer_create_valid():
    client = APIClient()
    url = reverse('killer-list')  # Matches the new killer-list route

    # Valid data for creation
    data = {
        'name': 'Freddy Krueger',
        'image_path': '/path/to/freddy.jpg'
    }

    response = client.post(url, data, format='json')

    # Check that the killer was created successfully
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'Freddy Krueger'
    assert response.data['image_path'] == '/path/to/freddy.jpg'

@pytest.mark.django_db
def test_killer_create_invalid():
    client = APIClient()
    url = reverse('killer-list')  # Matches the killer-list route

    # Invalid data (missing 'image_path')
    data = {
        'name': 'Freddy Krueger'
    }

    response = client.post(url, data, format='json')

    # Check that the request fails due to missing fields
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'error' in response.data

@pytest.mark.django_db
def test_killer_update_valid():
    client = APIClient()
    # Create a Killer instance to update
    killer = Killer.objects.create(name='Freddy Krueger', image_path='/path/to/freddy.jpg')
    url = reverse('killer-detail', kwargs={'pk': killer.pk})  # Matches killer-detail

    # Valid update data
    update_data = {
        'name': 'Jason Voorhees',
        'image_path': '/path/to/jason.jpg'
    }

    response = client.put(url, update_data, format='json')

    # Check that the update was successful
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Jason Voorhees'
    assert response.data['image_path'] == '/path/to/jason.jpg'

@pytest.mark.django_db
def test_killer_update_invalid():
    client = APIClient()
    # Create a Killer instance to update
    killer = Killer.objects.create(name='Freddy Krueger', image_path='/path/to/freddy.jpg')
    url = reverse('killer-detail', kwargs={'pk': killer.pk})  # Matches killer-detail

    # Invalid update data (missing 'image_path')
    update_data = {
        'name': 'Jason Voorhees'
    }

    response = client.put(url, update_data, format='json')

    # Check that the request fails due to missing fields
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'error' in response.data

@pytest.mark.django_db
def test_killer_delete():
    client = APIClient()
    # Create a Killer instance to delete
    killer = Killer.objects.create(name='Freddy Krueger', image_path='/path/to/freddy.jpg')
    url = reverse('killer-detail', kwargs={'pk': killer.pk})  # Matches killer-detail

    # Send delete request
    response = client.delete(url)

    # Check that the delete was successful
    assert response.status_code == status.HTTP_204_NO_CONTENT
    # Ensure the object is deleted
    assert Killer.objects.filter(pk=killer.pk).count() == 0

@pytest.mark.django_db
def test_random_killer_post():
    client = APIClient()
    # Create some Killer instances
    Killer.objects.create(name='Freddy Krueger', image_path='/path/to/freddy.jpg')
    Killer.objects.create(name='Jason Voorhees', image_path='/path/to/jason.jpg')

    url = reverse('killer-random')  # Matches killer-random route

    # Send POST request
    response = client.post(url, format='json')

    # Check that the response is successful and a random killer is returned
    assert response.status_code == status.HTTP_200_OK
    assert 'name' in response.data
    assert 'image_path' in response.data

@pytest.mark.django_db
def test_random_killer_get():
    client = APIClient()
    url = reverse('killer-random')  # Matches killer-random route

    # Send GET request (though random killer method only handles POST for now)
    response = client.get(url, format='json')

    # The GET request is only printing for now, check the print side-effect if necessary
    assert response.status_code == status.HTTP_200_OK
    # No actual return on GET, but it should not raise an error
