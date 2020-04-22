from django import forms

class NoteForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)
    lines = forms.CharField(label="Line(s)", max_length=40)
