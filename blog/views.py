from django.shortcuts import render
from django.shortcuts import get_object_or_404
from blog.models import Post, BlogCategory, Tag
from django.db.models import Count


# Create your views here.


def blog_list(request):
    blogs = Post.objects.exclude(status=0).select_related('blogCategory').prefetch_related('tags')
    categories = BlogCategory.objects.all()
    tags = Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    category = request.GET.get('category')
    tag = request.GET.get('tag')
    sort = request.GET.get('sort')
    status = request.GET.get('status')

    if category:
        blogs = blogs.filter(category__slug=category)

    if sort == 'newest':
        blogs = blogs.order_by('-created_at')
    elif sort == 'oldest':
        blogs = blogs.order_by('created_at')
    elif sort == 'title':
        blogs = blogs.order_by('title')

    if status:
        blogs = blogs.filter(status=status)

    if tag:
        blogs = blogs.filter(tags__slug=tag).distinct()

    context = {'blogs': blogs, 'category': category, 'tag': tag, 'tags': tags, 'categories': categories}
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    post = get_object_or_404(Post.objects.select_related('blogCategory').prefetch_related('tags'), slug=slug)
    context = {'post': post}
    return render(request, 'blog/blog_detail.html', context)
