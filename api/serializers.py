from rest_framework import serializers
from .models import Student, Professor, Assistant , Appointment,Room, RoomReservation, Reservation, Equipment

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
        fields = ['appointment_id','requester', 'receiver', 'time', 'day','status']



class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class RoomReservationSerializer(serializers.ModelSerializer):
    roomReservation_id = serializers.ReadOnlyField(source='id')
    # student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    class Meta:
        model = RoomReservation
        fields = ['roomReservation_id','requester','receiver','day', 'time', 'room','status']

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'