from django.urls import path
from .views import getRoutes, getNotes, updateNote, deleteNote, createNote, getNote, registerUser, loginUser

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('notes/', getNotes, name="notes"),
    path('notes/<str:pk>/update/', updateNote, name="update-note"),
    path('notes/<str:pk>/delete/', deleteNote, name="delete-note"),
    path('notes/create/', createNote, name="create-note"),
    path('notes/<str:pk>/', getNote, name="note"),
    path('register/', registerUser, name="register"),
    path('login/', loginUser, name="login"),
]
