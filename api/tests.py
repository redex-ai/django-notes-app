from django.test import TestCase
from rest_framework.test import APIClient
import logging

logger = logging.getLogger(__name__)

class NoteViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_getRoutes(self):
        logger.info("Starting test_getRoutes")
        try:
            response = self.client.get('/api/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data, {
                'notes': '/api/notes/',
                'create': '/api/notes/create/',
                'update': '/api/notes/update/<int:pk>/',
                'delete': '/api/notes/delete/<int:pk>/',
            })
            logger.info("test_getRoutes passed")
        except AssertionError as e:
            logger.error("test_getRoutes failed: %s", str(e))
            raise

    def test_getNotes(self):
        logger.info("Starting test_getNotes")
        try:
            response = self.client.get('/api/notes/')
            self.assertEqual(response.status_code, 200)
            # Assert the expected data format
            logger.info("test_getNotes passed")
        except AssertionError as e:
            logger.error("test_getNotes failed: %s", str(e))
            raise

    def test_getNote(self):
        logger.info("Starting test_getNote")
        try:
            # Create a test note
            response = self.client.get('/api/notes/1/')
            self.assertEqual(response.status_code, 200)
            # Assert the expected data format
            logger.info("test_getNote passed")
        except AssertionError as e:
            logger.error("test_getNote failed: %s", str(e))
            raise

    def test_updateNote(self):
        logger.info("Starting test_updateNote")
        try:
            # Create a test note
            response = self.client.put('/api/notes/update/1/', {'title': 'Updated Title', 'content': 'Updated Content'})
            self.assertEqual(response.status_code, 200)
            # Assert the expected data format
            logger.info("test_updateNote passed")
        except AssertionError as e:
            logger.error("test_updateNote failed: %s", str(e))
            raise

    def test_deleteNote(self):
        logger.info("Starting test_deleteNote")
        try:
            # Create a test note
            response = self.client.delete('/api/notes/delete/1/')
            self.assertEqual(response.status_code, 204)
            logger.info("test_deleteNote passed")
        except AssertionError as e:
            logger.error("test_deleteNote failed: %s", str(e))
            raise

    def test_createNote(self):
        logger.info("Starting test_createNote")
        try:
            response = self.client.post('/api/notes/create/', {'title': 'New Note', 'content': 'Note Content'})
            self.assertEqual(response.status_code, 201)
            # Assert the expected data format
            logger.info("test_createNote passed")
        except AssertionError as e:
            logger.error("test_createNote failed: %s", str(e))
            raise
