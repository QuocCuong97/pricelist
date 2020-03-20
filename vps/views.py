from django.shortcuts import render
from vps.models import VPS
# Create your views here.

def index(request):
    lst_pack = VPS.objects.all().order_by('vendor__name', 'price_3').values_list('vendor__name', 'vendor__logo', 'vendor__homepage', 'pack', 'price_3', 'vcpu', 'ssd', 'ram', 'link') 
    return render(request, 'vps/vps.html', {'list_pack': lst_pack})

