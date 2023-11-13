from django.urls import path
from .views import getRoutes, getNotes, updateNote, deleteNote, createNote, getNote, generate_hardcoded_tasks

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('notes/', getNotes, name="notes"),
    path('notes/<str:pk>/update/', updateNote, name="update-note"),
    path('notes/<str:pk>/delete/', deleteNote, name="delete-note"),
    path('notes/create/', createNote, name="create-note"),
    path('notes/<str:pk>/', getNote, name="note"),
    path('generate-tasks/', generate_hardcoded_tasks, name="generate-tasks"),
]
