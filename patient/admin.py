from django.contrib import admin
from . import models
# Register your models here.

class PatientModel(admin.ModelAdmin):
    list_display=['first_name','last_name','mobile','image']

    def first_name(self,obj):
        return obj.user.first_name
    def last_name(self,obj):
        return obj.user.last_name

admin.site.register(models.Patient,PatientModel)
