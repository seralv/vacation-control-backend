from django.db import models
from django.utils import timezone
from django.conf import settings

class Employee(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    position = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.last_name}"

class WorkInformation(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, related_name='work_information')
    entry_date = models.DateField(default=timezone.now)
    remaining_days = models.PositiveIntegerField(default=0)
    STATE_CHOICES = (
        ('vacation', 'Vacation'),
        ('working', 'Working'),
    )
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='working')

    def __str__(self):
        return f"{self.employee.name} {self.employee.last_name} - {self.state}"
    
    def update_state(self):
        today = timezone.now().date()
        vacations = VacationHistory.objects.filter(employee=self.employee, start_date__lte=today, end_date__gte=today)
        if vacations.exists():
            self.state = 'vacation'
        else:
            self.state = 'working'
        self.save()

    def calculate_remaining_days(self):
        today = timezone.now().date()
        years_of_service = (today - self.entry_date).days // 365
        if years_of_service < 1:
            self.remaining_days = 0
        elif years_of_service < 6:
            self.remaining_days = years_of_service * 15
        elif years_of_service < 11:
            self.remaining_days = 5 * 15 + (years_of_service - 5) * 20
        else:
            self.remaining_days = 5 * 15 + 5 * 20 + (years_of_service - 10) * 30
        used_vacation_days = VacationHistory.objects.filter(employee=self.employee).aggregate(total_days=models.Sum(models.F('end_date') - models.F('start_date')))['total_days']
        if used_vacation_days:
            used_days = used_vacation_days.days
            used_weekends = sum(a for d in (self.entry_date + timedelta(days=i) for i in range(used_days)) if d.weekday() == 6)
            self.remaining_days -= used_days - used_weekends
        self.save()

class VacationHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.employee.name} {self.employee.last_name} - {self.start_date} to {self.end_date}"
