from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from killer.models import Killer

class TestKillerView(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_get_killers(self):
        response = self.client.get('/api/killer', follow=True)
        assert response.status_code == 200

    def test_get_random_killer(self):
        response = self.client.get('/api/killer/random', follow=True)
        self.assertEqual(response.status_code, 200)
        assert len(response.data) == 1  # Expecting a single killer

    def test_create_killer(self):
        data = {
            "name": "New Killer",
            "image_path": "path/to/image.jpg",
            # Include other required fields
        }
        response = self.client.post('/api/killer/', data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, 201 ) # Created
        assert Killer.objects.filter(name="New Killer").exists()

    def test_update_killer(self):
        killer = Killer.objects.create(name='Old Killer', image_path='old.jpg')
        data = {'name': 'Updated Killer', 'image_path': 'new.jpg'}
        response = self.client.put(f'/api/killer/{killer.id}/', data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        killer.refresh_from_db()
        assert killer.name == 'Updated Killer'

    def test_delete_killer(self):
        killer = Killer.objects.create(name='Delete Killer', image_path='delete.jpg')
        response = self.client.delete(f'/api/killer/{killer.id}/')
        self.assertEqual(response.status_code, 204)
        assert not Killer.objects.filter(id=killer.id).exists()

class RandomKillerViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_random_survivor_endpoint(self):
        response = self.client.post('/api/killer/random/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response)
