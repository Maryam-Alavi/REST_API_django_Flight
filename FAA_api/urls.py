from django.urls import path
from . import views


urlpatterns = [

    path('DataSets/', views.GetData),
    path('AircraftModels/', views.GetAircraftModels),
    path('ActiveAircraft/AircraftManufacturer/', views.ActiveAircraftList),
    path('ActiveAircraft/AircraftModel', views.ActiveAircraftListModels),
    path('ReportOfActiveUser/', views.ReportOfActiveUserSum),
    path('PivotReportsSum/', views.PivotReportsSum),
]
