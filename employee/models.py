from django.db import models


class Employee_role(models.Model):
    id_position = models.AutoField(primary_key=True)
    name_position = models.CharField(verbose_name="Cargo", max_length=50)

    def __str__(self):
        return self.id_position

    class Meta:
        verbose_name = "Employee_rol"
        verbose_name_plural = "Employee_rols"
        db_table = "employee_rol"


class Employee(models.Model):
    id_number = models.AutoField(primary_key=True)
    identification_number = models.CharField(verbose_name="cedula", max_length=10, null=False, blank=False, unique=True)
    name = models.CharField(verbose_name="Nombre", max_length=50)
    last_name = models.CharField(verbose_name="Apellido", max_length=50)
    date_of_birth = models.DateField()
    assigned_boss = models.IntegerField()
    fk_employee_role = models.ForeignKey(Employee_role, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_number

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"
        db_table = 'employee'
