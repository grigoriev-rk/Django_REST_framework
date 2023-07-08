from rest_framework import serializers
from measurement.models import SensorModel, MeasurementModel


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorModel
        fields = ['id', 'name', 'description']


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementModel
        fields = ['temperature', 'created_at']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = SensorModel
        fields = ['id', 'name', 'description', 'measurements']


class MeasurementDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementModel
        fields = ['sensor', 'temperature', 'created_at']

