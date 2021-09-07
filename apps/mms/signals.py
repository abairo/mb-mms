from django.db.models.signals import pre_save
from django.core.signals import request_finished
from django.dispatch import receiver
from .models import MMS
from .utils.date import timestamp_to_datetime


@receiver(pre_save, sender=MMS)
def create_mms(sender, instance, *args, **kwargs):
    if not instance.pk:
        instance.date = timestamp_to_datetime(instance.timestamp)


request_finished.connect(create_mms, dispatch_uid='create_mms_a7c138bd')
