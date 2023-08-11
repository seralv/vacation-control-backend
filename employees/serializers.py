from rest_framework import serializers
from .models import Employee, WorkInformation, VacationHistory

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class WorkInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkInformation
        fields = '__all__'

class VacationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VacationHistory
        fields = '__all__'
