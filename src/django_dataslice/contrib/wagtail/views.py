from django.utils.translation import gettext_lazy as _
from generic_chooser.views import ModelChooserViewSet, ModelChooserMixin

from django_dataslice.models import DataSlice


class DataSliceChooserMixin(ModelChooserMixin):
    preserve_url_parameters = [
        "content_type",
    ]

    def get_unfiltered_object_list(self):
        objects = super().get_unfiltered_object_list()
        content_type = self.request.GET.get("content_type")
        if content_type:
            objects = objects.filter(pk=content_type)
        return objects


class DataSliceChooserViewSet(ModelChooserViewSet):
    icon = "user"
    model = DataSlice
    chooser_mixin_class = DataSliceChooserMixin
    page_title = _("Choose a data slice")
    per_page = 100
    order_by = "name"
    fields = ["name", "content_type"]
