from rest_framework import serializers
from .models import Student


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ['id', ]


class StudentListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'url', 'name', 'gender', 'number']
        read_only_fields = ['id', ]
