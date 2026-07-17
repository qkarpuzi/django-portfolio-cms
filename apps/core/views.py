from django.shortcuts import render
from .models import Profile


def home(request):
    profile = Profile.objects.first()
    context = {
        'profile': profile,
    }
    return render(request, 'core/home.html', context)