from django.shortcuts import render
from .models import Profile, Skill
from apps.services.models import Service


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    services = Service.objects.all()
    context = {
        'profile': profile,
        'skills': skills,
        'services': services,
    }
    return render(request, 'core/home.html', context)