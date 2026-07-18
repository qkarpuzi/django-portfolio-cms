from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill
from .forms import ContactForm
from apps.experience.models import Experience, Education, Certificate
from apps.projects.models import Project


def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    projects_count = Project.objects.count()
    context = {
        'profile': profile,
        'skills': skills,
        'projects_count': projects_count,
        'skills_count': skills.count(),
    }
    return render(request, 'core/home.html', context)

def about(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    certificates = Certificate.objects.all()
    context = {
        'profile': profile,
        'experiences': experiences,
        'education': education,
        'certificates': certificates,
    }
    return render(request, 'core/about.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for reaching out! I'll get back to you soon.")
            return redirect('core:contact')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    return render(request, 'core/contact.html', context)