from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.db import models
from grapple.helpers import register_query_field

from . import settings


@register_query_field("data_slice")
class DataSlice(models.Model):

    name = models.CharField(max_length=255, unique=True)
    filter = models.JSONField(null=True, blank=True, help_text="Django Queryset json configuration")
    content_type = models.ForeignKey(
        "contenttypes.ContentType",
        on_delete=models.CASCADE,
        limit_choices_to=settings.LIMIT_CHOICES_TO
    )

    def __str__(self):
        return str(self.name)

    def get_queryset(self, values=None):
        """
        TODO: Check that Content-Type is installed?

        :param values:
        :return:
        """
        ct = ContentType.objects.get_for_model(self.content_type.model_class())
        return ct.get_all_objects_for_this_type(**(self.filter or {}))

    def clean_filter(self):
        try:
            list(self.get_queryset())
        except Exception as e:
            raise ValidationError(f"Configuration has and error: {e}")
