from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

#class pour le user et tout ce qu'il y a en rapport avec le user
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

#class pour les matières
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

#class pour les salles de discussion
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name 

#class pour les messages écrit
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]

#class pour le user du calendrier
class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

#class cours    
class Venue(models.Model): 
    name = models.CharField('Venue Name', max_length=120)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    attendees = models.ManyToManyField(MyClubUser, blank=True) 

    def __str__(self): 
        return self.name    
    

#class événement
class Events(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)


    def __str__(self):
        return self.name

