from django import template

register = template.Library()


@register.filter
def reading_time(text, wpm=200):
    """
    Estimate reading time from plain text content.
    Usage: {{ post.content|reading_time }} -> "5 min read"
    """
    if not text:
        return "1 min read"

    word_count = len(text.split())
    minutes = max(1, round(word_count / wpm))
    return f"{minutes} min read"