import datetime
import random
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

@api_view(['GET'])
def generate_hardcoded_tasks(request):
    if request.method == 'GET':
        tasks = []
        for _ in range(50):
            task = {
                'title': generate_random_title(),
                'description': generate_random_description(),
                'due_date': generate_random_due_date(),
                'status': generate_random_status()
            }
            tasks.append(task)
        return Response(tasks)

def generate_random_title():
    titles = ['Task 1', 'Task 2', 'Task 3', 'Task 4', 'Task 5']
    return random.choice(titles)

def generate_random_description():
    descriptions = ['Lorem ipsum dolor sit amet', 'Consectetur adipiscing elit', 'Sed do eiusmod tempor incididunt', 'Ut labore et dolore magna aliqua', 'Ut enim ad minim veniam']
    return random.choice(descriptions)

def generate_random_due_date():
    start_date = datetime.date.today()
    end_date = start_date + datetime.timedelta(days=30)
    random_date = random.choice([start_date + datetime.timedelta(days=x) for x in range((end_date - start_date).days)])
    return random_date

def generate_random_status():
    statuses = ['Pending', 'In Progress', 'Completed']
    return random.choice(statuses)
