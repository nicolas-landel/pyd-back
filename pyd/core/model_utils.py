import uuid

from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords


class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(db_index=True, null=True)
    updated_at = models.DateTimeField(db_index=True, null=True)
    created_by = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Created by",
    )
    modified_by = models.ForeignKey(
        "users.User",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="%(class)s_modified_by",
        verbose_name="Modified by",
    )
    history = HistoricalRecords()

    class Meta:
        abstract = True
        get_latest_by = "created_at"
        ordering = ("-created_at",)

    def save(self, *args, **kwargs):
        now = timezone.now()
        if not self.created_at and self._state.adding:
            self.created_at = now
        if self.updated_at:
            self.updated_at = now
        return super().save(*args, **kwargs)