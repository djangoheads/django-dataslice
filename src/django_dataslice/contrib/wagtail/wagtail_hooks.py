from wagtail import hooks
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
)

from django_dataslice.contrib.wagtail import views
from django_dataslice.models import DataSlice


@hooks.register("register_admin_viewset")
def register_data_slice_chooser_viewset():
    return views.DataSliceChooserViewSet(
        "data_slice_chooser", url_prefix="data-slice-chooser"
    )


class DataSliceAdmin(ModelAdmin):
    model = DataSlice
    menu_label = "Data Slice"
    menu_icon = "table"
    list_display = ("name", )
