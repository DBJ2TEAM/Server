from rest_framework import serializers
from .models import Student, Professor, Assistant , Appointment,Room, RoomTimetable, RoomReservation, Reservation, Equipment

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

class AppointmentSerializer(serializers.ModelSerializer):
    appointment_id = serializers.ReadOnlyField(source='id')
    class Meta:
        model = Appointment
        fields = ['appointment_id','student', 'professor', 'time', 'day','status']
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class RoomTimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomTimetable
        fields = '__all__'

class RoomReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomReservation
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'