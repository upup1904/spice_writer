from django.urls import path
from . import views

urlpatterns = [
    path("add", views.add_liner_note, name='liner_note_add'),
    path("", views.index, name='liner_note_index'),
]
