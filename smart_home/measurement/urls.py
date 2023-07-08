from django.urls import path

from measurement.views import SensorList, SensorViewAndEdit, SensorMeasurements, AddSensor, AddMeasurement

urlpatterns = [
    path('sensors/', SensorList.as_view()),
    path('sensors/<id>/', SensorViewAndEdit.as_view()),
    path('sensors/<id>/measurements', SensorMeasurements.as_view()),
    path('add_sensor/', AddSensor.as_view()),
    path('add_measurement/', AddMeasurement.as_view()),
]
