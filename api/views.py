import datetime
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import NoteSerializer, UserSerializer
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

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
        {
            'Endpoint': '/register/',
            'method': 'POST',
            'body': {'username': "", 'email': "", 'password': ""},
            'description': 'Registers a new user'
        },
        {
            'Endpoint': '/login/',
            'method': 'POST',
            'body': {'username': "", 'password': ""},
            'description': 'Logs in a user'
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

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
