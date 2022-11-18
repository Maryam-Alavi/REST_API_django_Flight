from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Data, AircraftModels, ActiveAircraft, ReportOfActiveUser, PivotReports
from .serializers import ActiveAircraftSerializer


@api_view(['GET'])
def GetData(request):
    return JsonResponse(Data.alldata, safe=False)


@api_view(['GET'])
def GetAircraftModels(request):
    return Response(AircraftModels.needed_data)


@api_view(['GET'])
def ActiveAircraftList(request):
    return Response(ActiveAircraft.Data)


@api_view(['GET'])
def ActiveAircraftListModels(request):
    return Response(ActiveAircraft.Data)


@api_view(['GET'])
def ReportOfActiveUserSum(request):
    return Response(ReportOfActiveUser.Data)


@api_view(['GET'])
def PivotReportsSum(request):
    return Response(PivotReports.pivot)
