from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from functools import cached_property
from wagtail.blocks import ChooserBlock

from django_dataslice.contrib.wagtail.widgets import DataSliceChooser
from django_dataslice.models import DataSlice


@deconstructible
class SliceOf:
    model = ""

    def __init__(self, model=None):
        if model is not None:
            self.model = model

    def __call__(self, value):
        model_check = f"{value.content_type.app_label}.{value.content_type.model}"
        if self.model.lower() != model_check.lower():
            raise ValidationError(f"Slice is not type of {self.model}")

    def __eq__(self, other):
        return self.model


class DataSliceChooserBlock(ChooserBlock):

    @cached_property
    def target_model(self):
        return DataSlice

    @cached_property
    def widget(self):
        return DataSliceChooser()

    def get_form_state(self, value):
        return self.widget.get_value_data(value)
