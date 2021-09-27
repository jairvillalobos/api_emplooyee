from rest_framework import serializers
from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
                    'id_number',
                    'name',
                    'last_name',
                    'date_of_birth',
                    'assigned_boss',
                    'fk_employee_role',
                    'identification_number'
                ]
