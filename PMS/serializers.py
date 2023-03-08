from rest_framework import serializers
from .models import Building, Rows, Floor, Coloumn, Vehicle

#creating serializers.

class BuildingSerializers(serializers.ModelSerializer):
    class Meta:
        model=Building
        fields="__all__"
        # exclude=["building"]

class FloorSerializers(serializers.ModelSerializer):
    class Meta:
        model=Floor
        fields="__all__"

class RowsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Rows
        fields="__all__"

class ColoumnSerializers(serializers.ModelSerializer):
    class Meta:
        model=Coloumn
        fields="__all__"

class VehicleSerializers(serializers.ModelSerializer):
    class Meta:
        model=Vehicle
        fields="__all__"