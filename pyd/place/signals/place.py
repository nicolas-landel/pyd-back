from django.db.models.signals import post_save
from django.dispatch import receiver

from pyd.place.models import Calendar
from pyd.place.models import Place


@receiver(post_save, sender=Place)
def create_calendar_for_place(sender, instance, created, **kwargs):
    if created:
        Calendar.objects.get_or_create(place=instance)
