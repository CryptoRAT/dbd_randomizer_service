import pytest
from django.test import TestCase
from rest_framework import status
from perk.models import Perk

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
