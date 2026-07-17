from django.shortcuts import render
from .models import Profile, Skill


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    context = {
        'profile': profile,
        'skills': skills,
    }
    return render(request, 'core/home.html', context)