from django.urls import path
from . import views

urlpatterns = [
    path('', views.NoteList.as_view(), name='note_list'),
    path('new', views.NoteCreate.as_view(), name='note_new'),
    path('view/<int:pk>', views.NoteView.as_view(), name='note_view'),
    path('edit/<int:pk>', views.NoteUpdate.as_view(), name='note_edit'),
    path('delete/<int:pk>', views.NoteDelete.as_view(), name='note_delete'),
]