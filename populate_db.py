import os
import django
from faker import Faker
from datetime import timedelta
from django.utils import timezone

# Configuración de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vacation_system.settings")
django.setup()

from employees.models import Employee, WorkInformation, VacationHistory

fake = Faker()

def create_employee():
    name = fake.first_name()
    last_name = fake.last_name()
    address = fake.address()
    phone = fake.phone_number()[:6]
    position = fake.job()
    return Employee.objects.create(name=name, last_name=last_name, address=address, phone=phone, position=position)

def create_work_information(employee):
    entry_date = fake.date_between(start_date='-10y', end_date='today')
    return WorkInformation.objects.create(employee=employee, entry_date=entry_date)

def create_vacation_history(employee):
    start_date = fake.date_between(start_date='-2y', end_date='today')
    end_date = start_date + timedelta(days=fake.random_int(min=5, max=30))
    return VacationHistory.objects.create(employee=employee, start_date=start_date, end_date=end_date)

if __name__ == '__main__':
    for _ in range(20):  # Cambia el número según la cantidad de registros que deseas crear
        employee = create_employee()
        work_info = create_work_information(employee)
        if work_info.state == 'vacation':
            create_vacation_history(employee)
        work_info.calculate_remaining_days()
