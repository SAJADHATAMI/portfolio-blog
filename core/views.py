from django.shortcuts import render, redirect
from courses.models import Course
from blog.models import Post
from projects.models import Project
from contact.forms import ContactMessageForm
from django.contrib import messages  # ۱. ایمپورت کردن سیستم پیام‌ها
from django.urls import reverse

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message!')
            return redirect(reverse('home') + '#contact')
    else:
        form = ContactMessageForm()

    projects = Project.objects.exclude(status=0).select_related('category').prefetch_related('skills').order_by(
        '-created_at')[:6]
    blogs = Post.objects.exclude(status=0).select_related('blogCategory').prefetch_related('tags').order_by('-created_at')[
        :6]
    courses = Course.objects.all().select_related('skill', 'coach', 'source').order_by('-start_date')[:6]
    context = {'projects': projects, 'blogs': blogs, 'courses': courses, 'form': form}
    return render(request, 'core/index.html', context)