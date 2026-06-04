from django.shortcuts import render
from courses.models import Course
from blog.models import Post
from projects.models import Project


# Create your views here.
def home(request):
    projects = Project.objects.exclude(status=0).select_related('category').prefetch_related('skills').order_by(
        '-created_at')[:6]
    blogs = Post.objects.exclude(status=0).select_related('blogCategory').prefetch_related('tags').order_by('-created_at')[
        :6]
    courses = Course.objects.all().select_related('skill', 'coach', 'source').order_by('-start_date')[:6]
    context = {'projects': projects, 'blogs': blogs, 'courses': courses}
    return render(request, 'core/index.html', context)