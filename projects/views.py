from unicodedata import category

from django.shortcuts import render
from django.shortcuts import get_object_or_404

from projects.models import Project, Category


# Create your views here.



def projects_list(request):
    projects = Project.objects.exclude(status=0).select_related('category').prefetch_related('skills')
    categories = Category.objects.all()
    category = request.GET.get('category')
    sort = request.GET.get('sort')
    status = request.GET.get('status')

    if category:
        projects = projects.filter(category__slug=category)

    if sort == 'newest':
        projects = projects.order_by('-created_at')
    elif sort == 'oldest':
        projects = projects.order_by('created_at')
    elif sort == 'title':
        projects = projects.order_by('title')

    if status:
        projects = projects.filter(status=status)

    context = {'projects': projects, 'category': categories}
    return render(request, 'projects/projects_list.html', context)



def project_detail(request, slug):
    project = get_object_or_404(
        Project.objects.select_related('category').prefetch_related('skills'),
        slug=slug
    )
    context = {'project': project}
    return render(request, 'projects/project_detail.html', context)