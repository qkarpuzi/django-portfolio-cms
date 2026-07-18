from django.shortcuts import render
from .models import Service


def service_list(request):
    services = Service.objects.all()
    context = {
        'services': services,
    }
    return render(request, 'services/service_list.html', context)