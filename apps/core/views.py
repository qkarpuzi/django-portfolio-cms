from django.shortcuts import render
from .models import Profile, Skill
from apps.experience.models import Experience, Education


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    context = {
        'profile': profile,
        'skills': skills,
    }
    return render(request, 'core/home.html', context)


def about(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    context = {
        'profile': profile,
        'experiences': experiences,
        'education': education,
    }
    return render(request, 'core/about.html', context)