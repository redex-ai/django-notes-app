import datetime
import logging
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

logger = logging.getLogger(__name__)

@api_view(['GET'])
def getRoutes(request):
    logger.info("Entering getRoutes function")
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    logger.info("Exiting getRoutes function")
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    logger.info("Entering getNotes function")
    if request.method == 'GET':
        try:
            notes = Note.objects.all().order_by('-created')
            serializer = NoteSerializer(notes, many=True)
            logger.info("Exiting getNotes function")
            return Response(serializer.data)
        except Exception as e:
            logger.exception("An exception occurred in getNotes function")
            return Response(status=500)

@api_view(['GET'])
def getNote(request, pk):
    logger.info("Entering getNote function")
    if request.method == 'GET':
        try:
            note = Note.objects.get(id=pk)
            serializer = NoteSerializer(note, many=False)
            logger.info("Exiting getNote function")
            return Response(serializer.data)
        except Note.DoesNotExist:
            logger.warning("Note with id {} does not exist".format(pk))
            return Response(status=404)
        except Exception as e:
            logger.exception("An exception occurred in getNote function")
            return Response(status=500)

@api_view(['PUT'])
def updateNote(request, pk):
    logger.info("Entering updateNote function")
    if request.method == 'PUT':
        try:
            note = Note.objects.get(id=pk)
            serializer = NoteSerializer(instance=note, data=request.data)
            if serializer.is_valid():
                serializer.save(updated=datetime.now())  # Update the 'updated' field with current date and time
                logger.info("Exiting updateNote function")
                return Response(serializer.data)
            else:
                logger.warning("Invalid data received for updating note with id {}".format(pk))
                return Response(serializer.errors, status=400)
        except Note.DoesNotExist:
            logger.warning("Note with id {} does not exist".format(pk))
            return Response(status=404)
        except Exception as e:
            logger.exception("An exception occurred in updateNote function")
            return Response(status=500)

@api_view(['DELETE'])
def deleteNote(request, pk):
    logger.info("Entering deleteNote function")
    if request.method == 'DELETE':
        try:
            note = Note.objects.get(id=pk)
            note.delete()
            logger.info("Exiting deleteNote function")
            return Response('Note was deleted!')
        except Note.DoesNotExist:
            logger.warning("Note with id {} does not exist".format(pk))
            return Response(status=404)
        except Exception as e:
            logger.exception("An exception occurred in deleteNote function")
            return Response(status=500)

@api_view(['POST'])
def createNote(request):
    logger.info("Entering createNote function")
    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info("Exiting createNote function")
            return Response(serializer.data, status=201)
        else:
            logger.warning("Invalid data received for creating note")
            return Response(serializer.errors, status=400)
