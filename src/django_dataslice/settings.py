from django.conf import settings


LIMIT_CHOICES_TO = getattr(settings, "DATASLICE_LIMIT_CHOICES_TO", {})
