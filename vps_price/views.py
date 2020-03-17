from django.shortcuts import render
from vps_price.models import Vps
# Create your views here.

def index(request):
    lst_pack = Vps.objects.all().order_by('vendor__name', 'price_3').values_list('vendor__name', 'vendor__logo', 'vendor__homepage', 'pack', 'price_3', 'vcpu', 'ssd', 'ram', 'link') 
    return render(request, 'pages/vps.html', {'list_pack': lst_pack})

