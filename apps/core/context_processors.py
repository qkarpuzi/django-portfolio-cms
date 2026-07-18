from .models import SEOSettings


def seo_settings(request):
    return {
        'seo': SEOSettings.objects.first(),
    }