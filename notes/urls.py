from django.contrib import admin
from django.urls import path, include
from notes.views import *

urlpatterns = [
    path('home/', home),
    path('archived/', archivedNotes, name='archived'),
    path('createNote/', CreateNote, name='note creation'),
    path('createNoteTemp/', createNoteTemp, name='create note'),
    path('updateNote/<int:id>/', updateNoteTemp, name='update'),
    path('updateNotePost/<int:id>/', updateNotePost, name='update'),
    path('deleteNote/<int:id>/', deleteNote),
    path('archived/restoreNote/<int:id>/', restoreNote),
]
