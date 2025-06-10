from django.shortcuts import render
from .models import Notes

# Create your views here.
def list_notes(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes': all_notes})

def note_details(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request,'notes/note_details.html',{'note':note})