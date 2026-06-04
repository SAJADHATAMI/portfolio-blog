from django.shortcuts import render
from django.shortcuts import get_object_or_404
from core.models import Skill
from courses.models import Course, Source, Coach


# Create your views here.



def courses_list(request):
    courses = Course.objects.all().select_related('skill', 'coach', 'source')
    skills = Skill.objects.all()
    coachs = Coach.objects.all()
    sources = Source.objects.all()

    skill = request.GET.get('skill')
    coach = request.GET.get('coach')
    source = request.GET.get('source')
    sort = request.GET.get('sort')



    if skill:
        courses = courses.filter(skill__slug=skill)
    if coach:
        courses = courses.filter(coach__slug=coach)
    if source:
        courses = courses.filter(source__slug=source)

    if sort == 'newest':
        courses = courses.order_by('-start_date')
    elif sort == 'oldest':
        courses = courses.order_by('start_date')
    elif sort == 'title':
        courses = courses.order_by('title')

    context = {'courses': courses, 'skills': skills, 'coachs': coachs, 'sources': sources}
    return render(request, 'courses/course_list.html', context)




def course_detail(request, slug):
    course = get_object_or_404(Course.objects.select_related('skill', 'coach', 'source'), slug=slug)
    context = {'course': course}
    return render(request, 'courses/course_detail.html', context)