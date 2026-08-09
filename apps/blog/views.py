from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    published = Post.objects.filter(status='published')

    category = request.GET.get('category')
    if category:
        published = published.filter(category=category)

    featured_post = published.first()
    posts = published.exclude(pk=featured_post.pk) if featured_post else published

    context = {
        'featured_post': featured_post,
        'posts': posts,
        'category_choices': Post._meta.get_field('category').choices,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    context = {
        'post': post,
        'related_posts': Post.objects.filter(status='published', category=post.category).exclude(pk=post.pk)[:3],
    }
    return render(request, 'blog/post_detail.html', context)