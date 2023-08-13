from rest_framework import serializers
from .models import Employee, WorkInformation, VacationHistory

class WorkInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkInformation
        fields = '__all__' 

class EmployeeSerializer(serializers.ModelSerializer):
    work_information = WorkInformationSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'name', 'last_name', 'address', 'phone', 'position', 'work_information']

class VacationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = VacationHistory
        fields = '__all__'
