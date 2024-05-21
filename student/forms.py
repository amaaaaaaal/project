from django import forms
from .models import Post, Stage, Event, Logement, Transport

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields ="__all__"

class StageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields ="__all__"

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields ="__all__"

class LogementForm(forms.ModelForm):
    class Meta:
        model =Logement
        fields ="__all__"

class TransportForm(forms.ModelForm):
    class Meta:
        model = Transport
        fields ="__all__"