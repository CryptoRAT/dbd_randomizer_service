import pytest
from django.test import TestCase
from survivor.models import Survivor

@pytest.mark.django_db
class TestSurvivorView(TestCase):
    def test_get_survivors(self):
        response = self.client.get('/api/survivor', follow=True)
        assert response.status_code == 200

    def test_get_random_survivor(self):
        response = self.client.get('/api/survivor/random', follow=True)
        assert response.status_code == 200
        assert len(response.data) == 1  # Expecting a single survivor

    def test_create_survivor(self):
        data = {
            "name": "New Survivor",
            "image_path": "path/to/image.jpg",
            # Include other required fields
        }
        response = self.client.post('/api/survivor/', data, format='json', content_type='application/json')
        assert response.status_code == 201  # Created
        assert Survivor.objects.filter(name="New Survivor").exists()

    def test_create_survivor(self):
        data = {'name': 'Test Survivor', 'image_path': 'test.jpg'}
        response = self.client.post('/api/survivor/', data, format='json', content_type='application/json')
        assert response.status_code == 201
        assert Survivor.objects.filter(name='Test Survivor').exists()

    def test_update_survivor(self):
        survivor = Survivor.objects.create(name='Old Survivor', image_path='old.jpg')
        data = {'name': 'Updated Survivor', 'image_path': 'new.jpg'}
        response = self.client.put(f'/api/survivor/{survivor.id}/', data, format='json', content_type='application/json')
        assert response.status_code == 200
        survivor.refresh_from_db()
        assert survivor.name == 'Updated Survivor'

    def test_delete_survivor(self):
        survivor = Survivor.objects.create(name='Delete Survivor', image_path='delete.jpg')
        response = self.client.delete(f'/api/survivor/{survivor.id}/')
        assert response.status_code == 204
        assert not Survivor.objects.filter(id=survivor.id).exists()



