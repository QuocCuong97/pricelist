from django.shortcuts import render
from vps.models import VPS
# Create your views here.

def index():
    a = VPS.objects.all()
    return a
    # return render(request, 'pages/vps.html')


index()