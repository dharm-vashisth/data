from django.shortcuts import render
from .models import Notes
from django.http import Http404


# view for list of notes.
def list_notes(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})


# view for individual note.
def note_details(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note doesn't exists.")

    return render(request, 'notes/note_details.html', {'note': note})
