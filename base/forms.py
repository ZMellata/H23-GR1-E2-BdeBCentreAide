from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User, Venue, Events

#form pour les éléments du user
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

#form pour les éléments de la salle de discussion
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']

#form pour les éléments du user
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'avatar', 'username', 'email', 'bio']

#form pour créer des événement
class EventForm(ModelForm):
    class Meta:
        model = Events
        fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description')
        labels = {
            'name':'',#form-control --> bootstrap
            'event_date':'YYYY-MM-DD HH:MM:SS',
            'venue':'Cours',
            'manager':'Professeur',
            'attendees':'Participants',
            'description':'',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom de l\'évenement'}),#form-control --> bootstrap
            'event_date':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Date de l\'événement'}),
            'venue':forms.Select(attrs={'class':'form-select', 'placeholder':'Venue'}),
            'manager':forms.Select(attrs={'class':'form-select', 'placeholder':'Manager'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Attendees'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),


        }

#Form pour créer des cours
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'manager', 'attendees')
        labels = {
            'name':'',#form-control --> bootstrap
            'manager':'Professeur',
            'attendees':'Participants',
        }
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom du cours'}),#form-control --> bootstrap
            'manager':forms.Select(attrs={'class':'form-select', 'placeholder':'Manager'}),
            'attendees':forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Attendees'}),
            

        }        
