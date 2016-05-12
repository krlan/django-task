from django.shortcuts import render, get_object_or_404
from .models import *


def index(request):
    context = {
        'schools': School.objects.all(),
    }
    return render(request, 'school/index.html', context)


def school(request, slug, *args, **kwargs):
    context = {
        'object_list': Classroom.objects.filter(school__slug=slug),
        'school': get_object_or_404(School, slug=slug)
    }
    return render(request, 'school/school.html', context)


def classroom(request, slug, *args, **kwargs):
    context = {
        'object_list': Student.objects.filter(classroom__slug=slug),
        'classroom': get_object_or_404(Classroom, slug=slug)
    }
    return render(request, 'school/classroom.html', context)


def student(request, slug, *args, **kwargs):
    context = {
        'student': get_object_or_404(Student, slug=slug),
    }
    return render(request, 'school/student.html', context)
