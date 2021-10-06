from django.shortcuts import render

# Create your views here.
def home(request):
    #templates folder is already assumed because this app is registered in settings.py
    name = "Ryan"
    return render(request, 'booking/home.html', context={"user_first_name":name})

def about(request):
    return render(request, 'booking/about.html')