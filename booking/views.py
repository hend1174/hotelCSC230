from django.shortcuts import render
from django.views.generic import ListView
from .models import Room, Guest

ROOMS = [101,102,103,104]

# Create your views here.
class RoomList(ListView):
    model = Room

class GuestList(ListView):
    model = Guest

def home(request):
    #templates folder is already assumed because this app is registered in settings.py
    name = "Ryan"
    loggedin=False
    context = {"user_first_name":name, "rooms":ROOMS, "loggedin":loggedin}
    return render(request, 'booking/home.html', context=context)

def about(request):
    return render(request, 'booking/about.html')