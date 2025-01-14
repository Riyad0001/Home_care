from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
# Create your views here.

class AppoinmentViewSet(viewsets.ModelViewSet):
    queryset=models.Appoinment.objects.all()
    serializer_class=serializers.AppoinmentSerializer

    #custom query set make

    def get_queryset(self):
        queryset=super().get_queryset()
        patient_id=self.request.query_params.get('patient_id')
        if patient_id:
            queryset=queryset.filter(patient_id=patient_id)
        return queryset
    def get_queryset(self):
        queryset=super().get_queryset()
        doctor_id=self.request.query_params.get('doctor_id')
        if doctor_id:
            queryset=queryset.filter(doctor_id=doctor_id)
        return queryset

