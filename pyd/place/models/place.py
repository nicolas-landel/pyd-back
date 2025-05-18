from django.db import models
from django.utils.translation import gettext_lazy as _

from pyd.core.model_utils import BaseModel


class CountryEnum:
    FRANCE = "FRANCE"

    @classmethod
    def get_as_choices(cls):
        return [(cls.FRANCE, _(cls.FRANCE))]


class Place(BaseModel):
    name = models.CharField(max_length=255, default=_("Place"), verbose_name=_("Place"))
    address = models.TextField(default="", verbose_name=_("Address"), max_length=255)
    address_comment = models.TextField(
        default="", blank=True, verbose_name=_("Address comment")
    )
    zipcode = models.CharField(default="", max_length=5, verbose_name=_("Zipcode"))
    city_name = models.CharField(default="", max_length=50, verbose_name=_("City name"))
    country_name = models.CharField(
        default=CountryEnum.FRANCE,
        max_length=50,
        choices=CountryEnum.get_as_choices(),
        verbose_name=_("Country"),
    )
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    description = models.TextField(
        default="", blank=True, verbose_name=_("Description")
    )
    max_capacity = models.IntegerField(null=True, blank=True)
    double_beds = models.IntegerField(null=True, blank=True)
    simple_beds = models.IntegerField(null=True, blank=True)
    rooms = models.IntegerField(null=True, blank=True)

    # TODO : add image gallery

    def __str__(self):
        return f" Place {self.name}"
