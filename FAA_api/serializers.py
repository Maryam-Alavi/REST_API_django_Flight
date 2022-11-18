from rest_framework import serializers
from .models import Data, AircraftModels, ActiveAircraft, ReportOfActiveUser, PivotReports


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['alldata']


class AircraftModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AircraftModels
        fields = ['needed_data']


class ActiveAircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveAircraft
        fields = ['Data']


class ReportOfActiveUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportOfActiveUser
        fields = ['Data']

class PivotReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PivotReports
        fields = ['pivot']