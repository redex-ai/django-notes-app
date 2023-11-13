from django.urls import path
from .views import getRoutes, getNotes, updateNote, deleteNote, createNote, getNote, RegisterView, LoginView

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('notes/', getNotes, name="notes"),
    path('notes/<str:pk>/update/', updateNote, name="update-note"),
    path('notes/<str:pk>/delete/', deleteNote, name="delete-note"),
    path('notes/create/', createNote, name="create-note"),
    path('notes/<str:pk>/', getNote, name="note"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
]
