from django.db import models
from django.utils.translation import gettext_lazy as _

from pyd.core.model_utils import BaseModel


class Calendar(BaseModel):
    place = models.OneToOneField(
        "place.Place",
        on_delete=models.CASCADE,
        related_name="calendar",
        verbose_name=_("Place"),
    )

    def __str__(self) -> str:
        return f"Calendar for {self.place.name}"
