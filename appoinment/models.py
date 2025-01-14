from django.db import models
from patient.models import Patient
from doctor.models import Doctor,AvailableTime
# Create your models here.

APPOINMENT_TYPES={
    ('Offline','Offline'),
    ('Online','Online'),
}
APPOINMENT_STATUS={
    ('Completed','Completed'),
    ('Running','Running'),
    ('Pending','Pending'),
}

class Appoinment(models.Model):
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appoinment_type=models.CharField(choices=APPOINMENT_TYPES,max_length=20)
    appoinment_status=models.CharField(choices=APPOINMENT_STATUS,max_length=20,default='Pending')
    symptom=models.TextField()
    time=models.ForeignKey(AvailableTime,on_delete=models.CASCADE)
    cancel=models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor : {self.doctor.user.first_name}    ;   Patient : {self.patient.user.first_name}"

    


