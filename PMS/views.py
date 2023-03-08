from django.shortcuts import render

from PMS.serializers import BuildingSerializers, RowsSerializers, FloorSerializers, ColoumnSerializers,VehicleSerializers
from .models import Building, Rows, Floor, Coloumn, Vehicle
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class BuildingView(generics.ListCreateAPIView):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializers

class FloorView(generics.ListCreateAPIView):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializers

class RowsView(generics.ListCreateAPIView):
    queryset = Rows.objects.all()
    serializer_class = RowsSerializers

class ColoumnView(generics.ListCreateAPIView):
    queryset = Coloumn.objects.all()
    serializer_class = ColoumnSerializers

class VehicleView(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializers