from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentDetailSerializer, StudentListSerializer
from .models import Student
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentDetailSerializer
        return StudentListSerializer


class AuthView(APIView):
    """
    测试授权访问，返回"Hello, world!"

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        测试授权访问，返回"Hello, world!"
        """
        return Response({"message": "Hello, world!"})
