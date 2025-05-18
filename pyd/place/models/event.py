from dateutil.relativedelta import relativedelta
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from pyd.core.model_utils import BaseModel


class Event(BaseModel):
    calendar = models.ForeignKey(
        "place.Calendar",
        related_name="events",
        on_delete=models.CASCADE,
        verbose_name=_("Calendar"),
    )
    start_date = models.DateTimeField(verbose_name=_("Start date"))
    end_date = models.DateTimeField(verbose_name=_("End date"))
    name = models.CharField(
        max_length=255, default=_("Event"), verbose_name=_("Event name")
    )
    description = models.TextField(
        default="",
        verbose_name=_("Comment"),
        blank=True,
    )
    is_validated = models.BooleanField(default=False, verbose_name=_("Is validated"))

    tags = models.ManyToManyField(
        to="place.Tag",
        related_name="events",
        blank=True,
        verbose_name=_("Event tags"),
        through="place.eventTags",
    )

    def __str__(self):
        return f"Event {self.uuid}"
