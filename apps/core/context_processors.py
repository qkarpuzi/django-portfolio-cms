from .models import SEOSettings, SocialLink, Profile


def seo_settings(request):
    return {
        'seo': SEOSettings.objects.first(),
        'social_links': SocialLink.objects.all(),
        'profile': Profile.objects.first(),
    }