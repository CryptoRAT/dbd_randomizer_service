import pytest
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from perk.models import Perk


@pytest.fixture(autouse=True)
def clear_perk_table():
    # Clear the Perk table before each test
    Perk.objects.all().delete()

@pytest.mark.django_db
def test_perk_create_valid():
    client = APIClient()
    url = reverse('survivor-perks')  # Matches the survivor-perks route for creating perks

    # Valid data for creation
    data = {
        'name': 'Dead Hard',
        'owner': 'David King',
        'type': 'Survivor',
        'image_path': '/path/to/dead_hard.jpg'
    }

    response = client.post(url, data, format='json')

    # Check that the perk was created successfully
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == 'Dead Hard'
    assert response.data['owner'] == 'David King'
    assert response.data['type'] == 'Survivor'
    assert response.data['image_path'] == '/path/to/dead_hard.jpg'

@pytest.mark.django_db
def test_perk_create_invalid():
    client = APIClient()
    url = reverse('survivor-perks')  # Matches the survivor-perks route

    # Invalid data (missing required fields)
    data = {
        'name': 'Dead Hard'
    }

    response = client.post(url, data, format='json')

    # Check that the request fails due to missing fields
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'error' in response.data

@pytest.mark.django_db
def test_perk_update_valid():
    client = APIClient()
    # Create a Perk instance to update
    perk = Perk.objects.create(name='Dead Hard', owner='David King', type='Survivor', image_path='/path/to/dead_hard.jpg')
    url = reverse('perk-detail', kwargs={'pk': perk.pk})  # Matches perk-detail route

    # Valid update data
    update_data = {
        'name': 'Barbecue & Chili',
        'owner': 'Leatherface',
        'type': 'Killer',
        'image_path': '/path/to/bbq_chili.jpg'
    }

    response = client.put(url, update_data, format='json')

    # Check that the update was successful
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == 'Barbecue & Chili'
    assert response.data['owner'] == 'Leatherface'
    assert response.data['type'] == 'Killer'
    assert response.data['image_path'] == '/path/to/bbq_chili.jpg'

@pytest.mark.django_db
def test_perk_destroy():
    client = APIClient()
    # Create a Perk instance to delete
    perk = Perk.objects.create(name='Dead Hard', owner='David King', type='Survivor', image_path='/path/to/dead_hard.jpg')
    url = reverse('perk-detail', kwargs={'pk': perk.pk})  # Matches perk-detail route

    # Send delete request
    response = client.delete(url)

    # Check that the delete was successful
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Perk.objects.filter(pk=perk.pk).count() == 0

@pytest.mark.django_db
def test_survivor_perks():
    client = APIClient()
    Perk.objects.create(name='Dead Hard', owner='David King', type='Survivor', image_path='/path/to/dead_hard.jpg')
    Perk.objects.create(name='Barbecue & Chili', owner='Leatherface', type='Killer', image_path='/path/to/bbq_chili.jpg')
    url = reverse('survivor-perks')  # Matches the survivor-perks route

    response = client.get(url)

    # Check that only survivor perks are returned
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2
    assert response.data[0]['name'] == 'Dead Hard'
    assert response.data[1]['name'] == 'Barbecue & Chili'

@pytest.mark.django_db
def test_killer_perks():
    client = APIClient()
    Perk.objects.create(name='Dead Hard', owner='David King', type='Survivor', image_path='/path/to/dead_hard.jpg')
    Perk.objects.create(name='Barbecue & Chili', owner='Leatherface', type='Killer', image_path='/path/to/bbq_chili.jpg')
    url = reverse('killer-perks')  # Matches the killer-perks route

    response = client.get(url)

    # Check that only killer perks are returned
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Barbecue & Chili'

@pytest.mark.django_db
def test_random_survivor_perks():
    client = APIClient()
    Perk.objects.create(name='Dead Hard', owner='David King', type='Survivor', image_path='/path/to/dead_hard.jpg')
    Perk.objects.create(name='Sprint Burst', owner='Meg Thomas', type='Survivor', image_path='/path/to/sprint_burst.jpg')
    url = reverse('random-survivor-perks')  # Matches random-survivor-perks route

    response = client.get(url)

    # Check that 1 to 4 random survivor perks are returned
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) <= 4

@pytest.mark.django_db
def test_random_killer_perks():
    client = APIClient()
    Perk.objects.create(name='Barbecue & Chili', owner='Leatherface', type='Killer', image_path='/path/to/bbq_chili.jpg')
    Perk.objects.create(name='Hex: Ruin', owner='The Hag', type='Killer', image_path='/path/to/hex_ruin.jpg')
    url = reverse('random-killer-perks')  # Matches random-killer-perks route

    response = client.get(url)

    # Check that 1 to 4 random killer perks are returned
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) <= 4
