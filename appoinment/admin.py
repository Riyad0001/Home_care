from django.contrib import admin
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
from . import models
# Register your models here.
class AppoinmentAdmin(admin.ModelAdmin):
    list_display=['patient_name','doctor_name','appoinment_type','appoinment_status','symptom','time','cancel']

    def patient_name(self,obj):
        return obj.patient.user.first_name
    def doctor_name(self,obj):
        return obj.doctor.user.first_name

    def save_model(self,request,obj,form,change):
        obj.save()
        if obj.appoinment_status=="Running" and obj.appoinment_type=="Online":
            email_subject="Your Online Appoinment Running"
            email_body=render_to_string('confirmA.html',{'user':obj.patient.user,'doctor':obj.doctor})
            email=EmailMultiAlternatives(email_subject,'',to=[obj.patient.user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()



admin.site.register(models.Appoinment,AppoinmentAdmin)
