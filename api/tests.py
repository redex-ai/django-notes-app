import logging
from django.test import TestCase
from rest_framework.test import APIClient

logger = logging.getLogger(__name__)

class NoteViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_getRoutes(self):
        logger.info("Starting test_getRoutes")
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'notes': '/api/notes/',
            'create': '/api/notes/create/',
            'update': '/api/notes/update/<int:pk>/',
            'delete': '/api/notes/delete/<int:pk>/',
        })
        logger.info("Finished test_getRoutes")

    def test_getNotes(self):
        logger.info("Starting test_getNotes")
        response = self.client.get('/api/notes/')
        self.assertEqual(response.status_code, 200)
        # Assert the expected data format
        logger.info("Finished test_getNotes")

    def test_getNote(self):
        logger.info("Starting test_getNote")
        # Create a test note
        response = self.client.get('/api/notes/1/')
        self.assertEqual(response.status_code, 200)
        # Assert the expected data format
        logger.info("Finished test_getNote")

    def test_updateNote(self):
        logger.info("Starting test_updateNote")
        # Create a test note
        response = self.client.put('/api/notes/update/1/', {'title': 'Updated Title', 'content': 'Updated Content'})
        self.assertEqual(response.status_code, 200)
        # Assert the expected data format
        logger.info("Finished test_updateNote")

    def test_deleteNote(self):
        logger.info("Starting test_deleteNote")
        # Create a test note
        response = self.client.delete('/api/notes/delete/1/')
        self.assertEqual(response.status_code, 204)
        logger.info("Finished test_deleteNote")

    def test_createNote(self):
        logger.info("Starting test_createNote")
        response = self.client.post('/api/notes/create/', {'title': 'New Note', 'content': 'Note Content'})
        self.assertEqual(response.status_code, 201)
        # Assert the expected data format
        logger.info("Finished test_createNote")
