from generic_chooser.widgets import AdminChooser
from django.contrib.admin.utils import quote
from cms.wagtail_hooks import DataSliceAdmin
from django_dataslice.models import DataSlice


class DataSliceChooser(AdminChooser):
    model = DataSlice
    choose_one_text = "Choose a Data Slice"
    choose_another_text = "Choose another Data Slice"
    link_to_chosen_text = "Edit this Data Slice"
    choose_modal_url_name = "data_slice_chooser:choose"

    def get_edit_item_url(self, item):
        return DataSliceAdmin().url_helper.get_action_url("edit", quote(item.pk))
