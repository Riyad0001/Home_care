from django.shortcuts import render
from rest_framework import viewsets,pagination
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework import filters

# Create your views here.
from . import models
from . import serializers
class DoctorPagignation(pagination.PageNumberPagination):
    page_size=1
    page_size_query_param=page_size
    max_page_size=100

class AvailableTimeForSpeceficDoctor(filters.BaseFilterBackend):
    def filter_queryset(self,request,query_set,view):
        doctor_id=request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor=doctor_id)
        return query_set
class AvailableReviewForSpeceficDoctor(filters.BaseFilterBackend):
    def filter_queryset(self,request,query_set,view):
        doctor_id=request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor=doctor_id)
        return query_set

class DesignationViewSet(viewsets.ModelViewSet):
    queryset=models.Designation.objects.all()
    serializer_class=serializers.DesignationSerializer
class SpecializationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=models.Specialization.objects.all()
    serializer_class=serializers.SpecializationSerializer
class AvailableTimeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset=models.AvailableTime.objects.all()
    serializer_class=serializers.AvailableTimeSerializer
    filter_backends=[AvailableTimeForSpeceficDoctor]
class DoctorViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    queryset=models.Doctor.objects.all()
    serializer_class=serializers.DoctorSerializer
    pagination_class=DoctorPagignation
class ReviewViewSet(viewsets.ModelViewSet):
    queryset=models.Review.objects.all()
    serializer_class=serializers.ReviewSerializer
    filter_backends=[AvailableReviewForSpeceficDoctor]