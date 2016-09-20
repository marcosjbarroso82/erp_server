from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing Balances
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
