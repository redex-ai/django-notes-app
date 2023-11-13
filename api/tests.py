from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User

class NoteViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')

    def test_getRoutes(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'notes': '/api/notes/',
            'create': '/api/notes/create/',
            'update': '/api/notes/update/<int:pk>/',
            'delete': '/api/notes/delete/<int:pk>/',
        })

    def test_getNotes(self):
        response = self.client.get('/api/notes/')
        self.assertEqual(response.status_code, 200)
        # Assert the expected data format

    def test_getNote(self):
        # Create a test note
        response = self.client.get('/api/notes/1/')
        self.assertEqual(response.status_code, 200)
        # Assert the expected data format

    def test_updateNote(self):
        # Create a test note
        response = self.client.put('/api/notes/update/1/', {'title': 'Updated Title', 'content': 'Updated Content'})
        self.assertEqual(response.status_code, 200)
        # Assert the expected data format

    def test_deleteNote(self):
        # Create a test note
        response = self.client.delete('/api/notes/delete/1/')
        self.assertEqual(response.status_code, 204)

    def test_createNote(self):
        response = self.client.post('/api/notes/create/', {'title': 'New Note', 'content': 'Note Content'})
        self.assertEqual(response.status_code, 201)
        # Assert the expected data format

    def test_registerUser(self):
        response = self.client.post('/api/register/', {'username': 'newuser', 'email': 'newuser@example.com', 'password': 'newpassword'})
        self.assertEqual(response.status_code, 201)
        # Assert the expected data format

    def test_loginUser(self):
        response = self.client.post('/api/login/', {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        # Assert the expected data format
