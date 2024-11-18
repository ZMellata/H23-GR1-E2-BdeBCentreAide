from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse 
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import Room, Topic, Message, User
from .forms import RoomForm, UserForm, MyUserCreationForm
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Events, Venue
from .forms import VenueForm, EventForm

#méthode permettant de à l'utilisateur de se connecter
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "Veuillez rentrer un Email valide")

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "L'Email ou le mot de passe ne sont pas valide")

    context = {'page': page}
    return render(request, 'base/login_register.html', context)

#méthode permettant de à l'utilisateur de se déconnecter
def logoutUser(request):
    logout(request)
    return redirect('home')

#méthode permettant de à l'utilisateur de se créer un compte
def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Une erreur est survenue durant la creation du compte')
            messages.error(request, 'Votre mot de passe doit contenir au moins 10 caractères')

    return render(request, 'base/login_register.html', {'form': form})

#méthode qui correspond à la page d'accueil et tout ce qu'elle possède
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    rooms = Room.objects.filter(
        Q(topic__name__icontains =q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )

    topics = Topic.objects.all()[0:4]
    room_count = rooms.count()
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))[0:3]

    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'base/homeForum.html', context)

#méthode qui correspond au différentes salles de discussion et tout ce qu'elles possèdent
def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body'),
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    context = {'room':room, 'room_messages': room_messages, 'participants': participants}
    return render(request, 'base/roomForum.html', context)

#méthode qui correspond à la page du profil d'un utilisateur
def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms, 'room_messages': room_messages, 'topics': topics}
    return render(request, 'base/profile.html', context)

#méthode qui permet de créer une salle de discussion avec tout ce qu'elle possède
@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )
        return redirect('home')

    context = {'form': form, 'topics':topics}
    return render(request, 'base/room_forum.html', context)

#méthode qui permet de modifier une salle de discussion en changeant le titre ou la matière, seulement par l'hôte de la salle
@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.user != room.host:
        return HttpResponse("Vous n'etes pas permis ici !")

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context = {'form': form, 'topics': topics, 'room': room}
    return render(request, 'base/room_forum.html', context)

#méthode qui permet de supprimer une salle de discussion, seulement par l'hôte de la salle
@login_required(login_url='login')
def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("Vous n'etes pas permis ici !")

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})

#méthode qui permet de supprimer un message écrit par un utilisateur
@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("Vous n'etes pas permis ici !")

    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': message})

#méthode qui permet de modifier les informations d'un utilisateur comme sa photo de profil ou son email
@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    return render(request, 'base/update-user.html', {'form': form})

#méthode qui permet de mettre en place la liste des matières
def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request, 'base/topics.html', {'topics': topics})

#méthode qui permet de mettre en place la liste des derniers messages envoyés par les utilisateurs
def activityPage(request):
    room_messages = Message.objects.all()
    return render(request, 'base/activity.html', {'room_messages': room_messages})

#méthode permetant de supprimer un cours
def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list-venues')

#méthode permettant de supprimer les événements
def delete_event(request, event_id): 
    event = Events.objects.get(pk=event_id)
    event.delete()
    return redirect('list-events')

#modifier évenement 
def update_event(request, event_id):
    event = Events.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('list-events')
    
    return render(request, 'events/update_event.html', {'event':event, 'form':form})

#ajouter évenement 
def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST) #
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {'form':form, 'submitted':submitted})

#permet de modifier les cours
def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('list-venues')
    
    return render(request, 'events/update_venue.html', {'venue':venue, 'form':form})

def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)    
        return render(request, 'events/search_venues.html', {'searched':searched, 'venues':venues})
    else:
        return render(request, 'events/search_venues.html', {})


#affiche les information du cours prof, participants...
def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html', {'venue': venue})

#affiche les cours
def list_venues(request):
    venue_list = Venue.objects.all().order_by('name')
    return render(request, 'events/venue.html', {'venue_list': venue_list})

#permet d'ajouter un cours
def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST) #
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_venue.html', {'form':form, 'submitted':submitted})

#affiche les événements
def all_events(request):
    event_list = Events.objects.all().order_by('event_date') #querying database
    return render(request, 'events/event_list.html', {'event_list': event_list})

#Affiche le calendrier
def homeCalendrier(request, year=datetime.now().year, month=datetime.now().strftime('%B')): 
    name = "John"
    month = month.capitalize() # Rend month majuscule pcq sinon y'aura erreur
    # Convertir month de name à number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number) # Assure que month_number est int

    
    cal = HTMLCalendar().formatmonth(year, month_number)

    
    now = datetime.now()
    current_year = now.year

    
    time = now.strftime('%H:%M %p')

    return render(request,
                   'events/home.html', {
                    "name": name, 
                    "year": year, # context dictionary du backend au frontend
                    "month": month,
                    "month_number": month_number,
                    "cal": cal,
                    "current_year": current_year,
                    "time": time,
                   })
