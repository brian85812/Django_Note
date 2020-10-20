from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Note

class NoteList(ListView):
    model = Note

class NoteView(DetailView):
    model = Note

class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'content']

    success_url = reverse_lazy('note_list')

class NoteUpdate(UpdateView):
    model = Note
    fields = ['title', 'content']

    success_url = reverse_lazy('note_list')

class NoteDelete(DeleteView):
    model = Note

    success_url = reverse_lazy('note_list')





