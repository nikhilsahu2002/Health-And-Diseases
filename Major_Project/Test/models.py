
from djongo import models


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
    
class dataset(models.Model):
    Disease=models.CharField(max_length=255,default=' ')
    Symptom_1=models.CharField(max_length=255,default=' ')
    Symptom_2=models.CharField(max_length=255,default=' ')
    Symptom_3=models.CharField(max_length=255,default=' ')
    Symptom_4=models.CharField(max_length=255,default=' ')
    Symptom_5=models.CharField(max_length=255,default=' ')
    Symptom_6=models.CharField(max_length=255,default=' ')
    Symptom_7=models.CharField(max_length=255,default=' ')
    Symptom_8=models.CharField(max_length=255,default=' ')
    Symptom_9=models.CharField(max_length=255,default=' ')
    Symptom_10=models.CharField(max_length=255,default=' ')
    Symptom_11=models.CharField(max_length=255,default=' ')
    Symptom_12=models.CharField(max_length=255,default=' ')
    Symptom_13=models.CharField(max_length=255,default=' ')
    Symptom_14=models.CharField(max_length=255,default=' ')
    Symptom_15=models.CharField(max_length=255,default=' ')
    Symptom_16=models.CharField(max_length=255,default=' ')
    Symptom_17=models.CharField(max_length=255,default=' ')



