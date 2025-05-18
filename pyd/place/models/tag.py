from django.db import models
from django.utils.translation import gettext_lazy as _

from pyd.core.model_utils import BaseModel


class Tag(BaseModel):
    calendar = models.ForeignKey(
        "place.Calendar",
        related_name="tags",
        on_delete=models.CASCADE,
        verbose_name=_("Calendar"),
    )
    name = models.CharField(
        max_length=255,
        default=_("Tag"),
        verbose_name=_("Tag name"),
    )
    description = models.TextField(
        default="",
        verbose_name=_("Tag description"),
        blank=True,
    )

    def __str__(self):
        return f"Tag {self.name}"


class EventTags(BaseModel):
    event = models.ForeignKey(
        "place.Event",
        related_name="event_tags",
        on_delete=models.CASCADE,
        verbose_name=_("Event"),
    )
    tag = models.ForeignKey(
        "place.Tag",
        related_name="event_tags",
        on_delete=models.CASCADE,
        verbose_name=_("Tag"),
    )

    def __str__(self):
        return f"EventTags {self.event.uuid!s} - {self.tag.name}"
