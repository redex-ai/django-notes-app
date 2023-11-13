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
    logger.info("GET request received for getRoutes")
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
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    logger.info("GET request received for getNotes")
    if request.method == 'GET':
        notes = Note.objects.all().order_by('-created')
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    logger.info(f"GET request received for getNote with pk={pk}")
    if request.method == 'GET':
        try:
            note = Note.objects.get(id=pk)
            serializer = NoteSerializer(note, many=False)
            return Response(serializer.data)
        except Note.DoesNotExist:
            logger.error(f"Note with pk={pk} does not exist")
            return Response(status=404)

@api_view(['PUT'])
def updateNote(request, pk):
    logger.info(f"PUT request received for updateNote with pk={pk}")
    if request.method == 'PUT':
        try:
            note = Note.objects.get(id=pk)
            serializer = NoteSerializer(instance=note, data=request.data)
            if serializer.is_valid():
                serializer.save(updated=datetime.now())  # Update the 'updated' field with current date and time
                return Response(serializer.data)
            else:
                logger.error(f"Invalid data provided for updateNote with pk={pk}")
                return Response(serializer.errors, status=400)
        except Note.DoesNotExist:
            logger.error(f"Note with pk={pk} does not exist")
            return Response(status=404)

@api_view(['DELETE'])
def deleteNote(request, pk):
    logger.info(f"DELETE request received for deleteNote with pk={pk}")
    if request.method == 'DELETE':
        try:
            note = Note.objects.get(id=pk)
            note.delete()
            return Response('Note was deleted!')
        except Note.DoesNotExist:
            logger.error(f"Note with pk={pk} does not exist")
            return Response(status=404)

@api_view(['POST'])
def createNote(request):
    logger.info("POST request received for createNote")
    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            logger.error("Invalid data provided for createNote")
            return Response(serializer.errors, status=400)
