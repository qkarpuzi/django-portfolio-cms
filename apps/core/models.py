from django.db import models

# Create your models here.
class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=150, help_text="e.g. Full Stack Django Developer")
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume = models.FileField(upload_to='resume/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name
    

class Skill(models.Model):
    PROFICIENCY_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    ]

    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skills/', blank=True, null=True, help_text="Upload a small logo/icon image")
    proficiency = models.CharField(max_length=20, choices=PROFICIENCY_CHOICES, default='intermediate')
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.subject} — from {self.name}"
    

class SEOSettings(models.Model):
    site_title = models.CharField(max_length=100, default="My Portfolio")
    meta_description = models.CharField(max_length=300, help_text="Shown in search engine results (recommended: under 160 characters)")
    meta_keywords = models.CharField(max_length=300, blank=True, help_text="Comma-separated keywords (optional, low SEO impact today)")
    og_image = models.ImageField(upload_to='seo/', blank=True, null=True, help_text="Image shown when your site is shared on social media (recommended: 1200x630px)")

    class Meta:
        verbose_name = "SEO Settings"
        verbose_name_plural = "SEO Settings"

    def __str__(self):
        return "SEO Settings"