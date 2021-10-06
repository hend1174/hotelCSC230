from django.shortcuts import render

# Create your views here.
def home(request):
    #templates folder is already assumed because this app is registered in settings.py
    return render(request, 'booking/home.html')