from django.shortcuts import render
from rest_framework import viewsets
from .models import Employee, WorkInformation, VacationHistory
from .serializers import EmployeeSerializer, WorkInformationSerializer, VacationHistorySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class WorkInformationViewSet(viewsets.ModelViewSet):
    queryset = WorkInformation.objects.all()
    serializer_class = WorkInformationSerializer

class VacationHistoryViewSet(viewsets.ModelViewSet):
    queryset = VacationHistory.objects.all()
    serializer_class = VacationHistorySerializer
