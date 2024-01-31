from rest_framework.test import APIClient
from rest_framework import status
import pytest
from django.test import TestCase
from perk.models import Perk

class RandomSurvivorPerkViewTestCase(TestCase):

    def setUp(self):
        # Set up any necessary data for your tests
        self.client = APIClient()

    def test_random_survivor_perk_endpoint(self):
        # Test your view logic here
        response = self.client.post('/api/perk/survivor/random/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the response data is a list
        self.assertIsInstance(response.data, list)

        # Check if each perk in the response has a type of 'Survivor'
        for perk_data in response.data:
            self.assertEqual(perk_data['type'], 'Survivor')

class RandomKillerPerkViewTestCase(TestCase):

    def setUp(self):
        # Set up any necessary data for your tests
        self.client = APIClient()

    def test_random_killer_perk_endpoint(self):
        # Test your view logic here
        response = self.client.post('/api/perk/killer/random/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the response data is a list
        self.assertIsInstance(response.data, list)

        # Check if each perk in the response has a type of 'Survivor'
        for perk_data in response.data:
            self.assertEqual(perk_data['type'], 'Killer')



@pytest.mark.django_db
class TestPerkViews(TestCase):

    def test_create_perk(self):
        data = {'name': 'Test Perk', 'owner': 'Test Owner', 'type': 'Survivor', 'image_path': 'test.jpg'}
        response = self.client.post('/api/survivor/perks/', data, format='json', content_type='application/json')
        assert response.status_code == status.HTTP_201_CREATED

    def test_update_perk(self):
        perk = Perk.objects.create(name='Old Perk', owner='Old Owner', type='Survivor', image_path='old.jpg')
        data = {'name': 'Updated Perk', 'owner': 'Updated Owner', 'type': 'Survivor', 'image_path': 'new.jpg'}
        response = self.client.put(f'/api/survivor/perks/{perk.id}/', data, format='json', content_type='application/json')
        print(response.status_code)
        assert response.status_code == status.HTTP_200_OK
        perk.refresh_from_db()
        assert perk.name == 'Updated Perk'

    def test_delete_perk(self):
        perk = Perk.objects.create(name='To be deleted', owner='Test Owner', type='Survivor', image_path='test.jpg')
        response = self.client.delete(f'/api/survivor/perks/{perk.id}/')
        assert response.status_code == status.HTTP_204_NO_CONTENT
