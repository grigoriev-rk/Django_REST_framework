from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from measurement.models import SensorModel, MeasurementModel
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer, MeasurementDetailSerializer
from rest_framework.response import Response


class SensorList(ListAPIView):
    queryset = SensorModel.objects.all()
    serializer_class = SensorSerializer
    lookup_field = 'id'


class SensorViewAndEdit(RetrieveAPIView):
    queryset = SensorModel.objects.all()
    serializer_class = SensorDetailSerializer
    lookup_field = 'id'

    def put(self, request, pk):
        sensor = SensorModel.objects.get(id=pk)
        sensor.description = request.data['description']
        sensor.save()
        return Response({'status': 'OK'})


class SensorMeasurements(RetrieveAPIView):
    queryset = SensorModel.objects.all()
    serializer_class = SensorDetailSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        sensor = self.get_object()
        serializer = self.get_serializer(sensor)
        data = serializer.data
        measurements = MeasurementModel.objects.filter(sensor=sensor)
        measurement_serializer = MeasurementSerializer(measurements, many=True)
        data['measurements'] = measurement_serializer.data
        return Response(data)


class AddMeasurement(CreateAPIView):
    queryset = MeasurementModel.objects.all()
    serializer_class = MeasurementDetailSerializer


class AddSensor(CreateAPIView):
    queryset = SensorModel.objects.all()
    serializer_class = SensorDetailSerializer

    def post(self, request):
        SensorModel.objects.create(
            name=request.POST.get('name'),
            description=request.POST.get('description'))
        return Response({'status': 'OK'})
