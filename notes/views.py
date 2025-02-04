from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Note

@csrf_exempt
def notes_list(request):
    if request.method == 'GET':
        notes = list(Note.objects.values('id', 'title', 'content', 'createdAt'))
        return JsonResponse(notes, safe=False)
    
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            note = Note.objects.create(title=data['title'], content=data['content'])
            return JsonResponse({'id': note.id, 'title': note.title, 'content': note.content,'createdAt': note.createdAt}, status=201)
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid data'}, status=400)

@csrf_exempt
def note_detail(request, id):
    try:
        note = Note.objects.get(id=id)
    except Note.DoesNotExist:
        return JsonResponse({'error': 'Note not found'}, status=404)
    
    if request.method == 'GET':
        return JsonResponse({'id': note.id, 'title': note.title, 'content': note.content,'createdAt': note.createdAt})
    
    elif request.method == 'DELETE':
        note.delete()
        return JsonResponse({'message': 'Note deleted successfully'}, status=204)
