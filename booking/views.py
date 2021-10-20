from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from .models import Room, Guest
from .forms import GuestCreateForm, GuestUpdateForm

class GuestDelete(DeleteView):
    model = Guest
    template_name = 'booking/guest_delete_form.html'
    success_url = '/guestlist'

class GuestUpdate(UpdateView):
    model = Guest
    template_name = 'booking/guest_update_form.html'
    form_class = GuestUpdateForm

class GuestCreate(CreateView):
    model = Guest
    template_name = 'booking/guest_create_form.html'
    form_class = GuestCreateForm

# Create your views here.
class RoomList(ListView):
    model = Room

class GuestList(ListView):
    model = Guest

def home(request):
    # templates folder is already assumed because this app is registered in settings.py
    name = "Ryan"
    loggedin=False
    context = {"user_first_name":name, "rooms":ROOMS, "loggedin":loggedin}
    return render(request, 'booking/home.html', context=context)

def about(request):
    return render(request, 'booking/about.html')