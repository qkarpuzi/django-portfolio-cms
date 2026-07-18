from .models import SEOSettings, SocialLink


def seo_settings(request):
    return {
        'seo': SEOSettings.objects.first(),
        'social_links': SocialLink.objects.all(),
    }