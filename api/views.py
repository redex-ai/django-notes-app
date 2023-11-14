import datetime
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note

@api_view(['GET'])
def getRoutes(request):
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
            'body': {'title': "", 'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'title': "", 'body': ""},
            'description': 'Updates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing note'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    if request.method == 'GET':
        notes = Note.objects.all().order_by('-created')
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    if request.method == 'GET':
        try:
            note = Note.objects.get(id=pk)
            serializer = NoteSerializer(note, many=False)
            return Response(serializer.data)
        except Note.DoesNotExist:
            return Response(status=404)

@api_view(['PUT'])
def updateNote(request, pk):
    if request.method == 'PUT':
        try:
            note = Note.objects.get(id=pk)
            serializer = NoteSerializer(instance=note, data=request.data)
            if serializer.is_valid():
                serializer.save(updated=datetime.now())  # Update the 'updated' field with current date and time
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=400)
        except Note.DoesNotExist:
            return Response(status=404)

@api_view(['DELETE'])
def deleteNote(request, pk):
    if request.method == 'DELETE':
        try:
            note = Note.objects.get(id=pk)
            note.delete()
            return Response('Note was deleted!')
        except Note.DoesNotExist:
            return Response(status=404)

@api_view(['POST'])
def createNote(request):
    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
