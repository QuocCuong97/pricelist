from django.shortcuts import render
from .models import Vps
# Create your views here.

def index():
    a = Vps.objects.all()
    return a
    # return render(request, 'pages/Vps.html')


# index()