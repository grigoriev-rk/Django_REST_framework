from django.contrib import admin
from measurement.models import SensorModel, MeasurementModel


# Register your models here.

@admin.register(SensorModel)
class SensorAdmin(admin.ModelAdmin):
    pass


@admin.register(MeasurementModel)
class MeasurementAdmin(admin.ModelAdmin):
    pass


