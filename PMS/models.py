from django.db import models
from account.models import User

# Create your models here.

class Building(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,)
    building_name = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    total_floors = models.PositiveIntegerField(default=2)
    total_rows = models.PositiveIntegerField(default=10)
    total_coloumn = models.PositiveIntegerField()  

class Floor(models.Model):
    building_id = models.ForeignKey(Building,on_delete=models.CASCADE,)
    floor_name = models.CharField(max_length=40)

class Rows(models.Model):
    building_id = models.ForeignKey(Building,on_delete=models.CASCADE,)
    floor_id = models.ForeignKey(Floor,on_delete=models.CASCADE,)
    Row_name = models.CharField(max_length=50)

class Coloumn(models.Model):
    building_id = models.ForeignKey(Building,on_delete=models.CASCADE,)
    floor_id = models.ForeignKey(Floor,on_delete=models.CASCADE,)
    rows_id = models.ForeignKey(Rows,on_delete=models.CASCADE,)
    coloumn_name = models.CharField(max_length=40)

class Vehicle(models.Model):
    types = (
        ("two wheeler", 'two wheeler'),
        ("three wheeler", 'three wheeler'),
        ("Four wheeler", 'Four wheeler')
    )
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,)
    vechile_name = models.CharField(max_length=40)
    vechile_type = models.CharField(choices=types, max_length=30)
    vechile_no = models.CharField(max_length=40)