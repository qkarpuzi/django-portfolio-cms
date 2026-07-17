from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=50, unique=True)
    icon = models.ImageField(upload_to='technologies/', blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Technologies'

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL-friendly version of the title, e.g. 'my-cool-app'")
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    technologies = models.ManyToManyField(Technology, related_name='projects', blank=True)
    thumbnail = models.ImageField(upload_to='projects/thumbnails/')
    live_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/screenshots/')
    caption = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.project.title} - Image {self.pk}"