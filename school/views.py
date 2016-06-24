from django.shortcuts import render, get_object_or_404
from .models import *
from .serializers import SchoolSerializer, ClassroomSerializer, StudentSerializer
from rest_framework import viewsets



class SchoolViewSet(viewsets.ModelViewSet):
    model = School
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class ClassroomViewSet(viewsets.ModelViewSet):
    model = Classroom
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class StudentViewSet(viewsets.ModelViewSet):
    model = Student
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


def index(request):
    return render(request, 'school/index.html')

