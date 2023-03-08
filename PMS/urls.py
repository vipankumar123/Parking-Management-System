from django.urls import path
from .views import BuildingView, RowsView, FloorView, ColoumnView, VehicleView

urlpatterns = [
    path("building/", BuildingView.as_view(), name = "building"),
    path("floor/", FloorView.as_view(), name = "floor"),
    path("rows/", RowsView.as_view(), name = "rows"),
    path("coloumn/", ColoumnView.as_view(), name = "coloumn"),
    path('vehicle/', VehicleView.as_view()),
]