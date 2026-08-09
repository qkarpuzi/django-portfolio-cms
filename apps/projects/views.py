from django.shortcuts import render, get_object_or_404
from .models import Project


def project_list(request):
    context = {
        'projects': Project.objects.all(),
        'category_choices': Project._meta.get_field('category').choices,
    }
    return render(request, 'projects/project_list.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {
        'project': project,
        'related_projects': Project.objects.exclude(pk=project.pk)[:3],
    }
    return render(request, 'projects/project_detail.html', context)