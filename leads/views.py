from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics
from django.shortcuts import render



# Create your views here.

class LeadListCreate(generics.ListCreateAPIView):
    queryset= Lead.objects.all()
    serializer_class = LeadSerializer

    