from django.contrib import admin

# Register your models here.

from .models import Room, Topic, Message, User

#en rapport avec la section "admin" de notre site
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)