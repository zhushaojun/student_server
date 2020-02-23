from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentDetailSerializer, StudentListSerializer
from .models import Student


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentDetailSerializer
        return StudentListSerializer
