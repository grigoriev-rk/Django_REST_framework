from django.db import models


class SensorModel(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название датчика')
    description = models.CharField(max_length=100, verbose_name='Описание датчика')


    class Meta:
        verbose_name = 'Сенсор'
        verbose_name_plural = 'Сенсоры'

    def __str__(self):
        return self.name


class MeasurementModel(models.Model):
    sensor = models.ForeignKey(SensorModel, on_delete=models.CASCADE, verbose_name='Название датчика')
    temperature = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ('created_at',)


