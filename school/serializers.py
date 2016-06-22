from rest_framework import serializers
from school.models import School, Classroom, Student


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'img')


class ClassroomSerializer(serializers.HyperlinkedModelSerializer):
    school = SchoolSerializer()

    class Meta:
        model = Classroom
        fields = ('id', 'number', 'school')


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    classroom = ClassroomSerializer()

    class Meta:
        model = Student
        fields = ('id', 'name', 'classroom')
