from allauth.account.decorators import secure_admin_login
from django.conf import settings
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.utils.translation import gettext_lazy as _

from .models import Calendar
from .models import Event
from .models import EventTags
from .models import Place
from .models import Tag

admin.autodiscover()


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "address"]
    search_fields = ["name", "description"]
    list_filter = ["created_at", "updated_at"]
    ordering = ["-created_at"]


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "start_date", "end_date", "created_by"]
    search_fields = ["name", "description", "created_by__email", "place__name"]
    ordering = ["-created_at"]


@admin.register(EventTags)
class EventTagsAdmin(admin.ModelAdmin):
    list_display = ["event", "tag"]
    search_fields = ["event__name", "tag__name"]
    ordering = ["-created_at"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]
    search_fields = ["name", "description"]
    ordering = ["-created_at"]


@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ["place"]
    ordering = ["-created_at"]
