from django.db import models


# Create your models here.


class Employee(models.Model):
    fname = models.CharField(max_length=80, verbose_name='First Name', default="")
    lname = models.CharField(max_length=80, verbose_name='Last Name', default="")
    rcode = models.CharField(max_length=5, db_index=True, unique=True, verbose_name='Employee Report code', default="")

    def set_rcode(self):
        rcod = self.fname[0] + self.lname[0]
        return rcod

    def save(self, *args, **kwargs):
        self.set_rcode()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.fname} {self.lname} ({self.rcode})"


class Report(models.Model):
    ASC = 'A'
    BASC = 'B'
    rchoices = [
        (ASC, 'ASC'),
        (BASC, 'BASC'),
    ]
    rnumber = models.PositiveIntegerField(db_index=True, unique=True, verbose_name='Report Number', null=True)
    name = models.CharField(max_length=120, verbose_name='Client Name', default="")
    rtype = models.CharField(max_length=1, choices=rchoices, verbose_name='Type of Report', default="")
    roperator = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL, verbose_name='Report Operator')

    def __str__(self):
        return f"{self.rnumber}"
