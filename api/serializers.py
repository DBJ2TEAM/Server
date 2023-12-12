from rest_framework import serializers
from .models import Student, Professor, Assistant ,TimeTable, Appointment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class AssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistant
        fields = '__all__'


class TimeTableSerializer(serializers.ModelSerializer):
    timetable_id = serializers.ReadOnlyField(source='id')
    class Meta:
        model = TimeTable
        fields = ['timetable_id', 'professor', 'start_time', 'end_time']

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id','student', 'professor', 'time', 'status']