from django.urls import path
from .views import notes_list
from .views import note_detail

urlpatterns = [
    path('api/notes/', notes_list, name='notes_list'),
    path('api/notes/<int:id>/', note_detail, name='note_detail'),
]
