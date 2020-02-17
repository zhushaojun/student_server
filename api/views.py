from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
