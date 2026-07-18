from django.contrib import admin
from .models import Profile, Skill, ContactMessage
from .models import Profile, Skill, ContactMessage, SEOSettings
from .models import Profile, Skill, ContactMessage, SEOSettings, SocialLink

admin.site.register(Profile)
admin.site.register(SEOSettings)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'proficiency', 'order']
    list_editable = ['proficiency', 'order']
    ordering = ['order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read']
    list_editable = ['is_read']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'order']
    list_editable = ['order']