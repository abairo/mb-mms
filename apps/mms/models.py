from django.db import models


class MMS(models.Model):
    pair = models.CharField(max_length=6)
    timestamp = models.IntegerField()
    mms_20 = models.DecimalField(max_digits=10, decimal_places=2)
    mms_50 = models.DecimalField(max_digits=10, decimal_places=2)
    mms_200 = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.pair} - {self.timestamp}'

    class Meta:
        verbose_name = 'MMS'
        verbose_name_plural = 'MMS'
