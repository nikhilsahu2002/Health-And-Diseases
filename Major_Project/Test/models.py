from django.db import models


# Create your models here.
class persion(models.Model):
    name = models.CharField(max_length=12500)
    sysptoms = models.CharField(max_length=12500)
    Desc =models.CharField(max_length=12500)
    commonTestsAndProceduresDesc = models.CharField(max_length=12500)
    commonTestsAndProcedures = models.CharField(max_length=12500)
    commonMedicationsDesc = models.CharField(max_length=12500)
    commonMedications = models.CharField(max_length=12500)
    whoIsAtRiskDesc = models.CharField(max_length=12500)
    symptomsDesc = models.CharField(max_length=12500)

    def __str__(self):
        return self.name
