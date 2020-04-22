from django.http import HttpResponse
from django.shortcuts import render
from .models import LinerNote, Line
from .forms import NoteForm
from liner_note import add_note


# Create your views here.

def index(request):
    return HttpResponse("SHUCKS I GUESS YOU GOT TO THE LINER NOTES!")


def add_liner_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            add_note.process_form(form)
            return HttpResponse('thanks')
        else:
            raise Exception("It was not good")
    else:
        form = NoteForm()
        return render(request, 'new_note.html', {'form': form})
