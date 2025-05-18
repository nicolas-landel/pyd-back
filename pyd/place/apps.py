from django.apps import AppConfig


class PlaceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pyd.place"

    def ready(self):
        import pyd.place.signals.place
        # import pyd.place.signals.tag
        # import pyd.place.signals.calendar
