from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, WorkInformationViewSet, VacationHistoryViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'work-information', WorkInformationViewSet)
router.register(r'vacation-history', VacationHistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
