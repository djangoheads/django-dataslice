from django.apps import apps
from grapple.models import GraphQLField
from grapple.registry import registry


def GraphQLQueryset(field_name, content_type, **kwargs):
    def Mixin():
        field_type = None
        if isinstance(content_type, str):
            app_label, model = content_type.lower().split(".")
            mdl = apps.get_model(app_label, model)
            if mdl:
                field_type = lambda: registry.models.get(mdl)  # noqa: E731
        else:
            field_type = lambda: registry.models.get(content_type)  # noqa: E731
        return GraphQLField(field_name, field_type, **kwargs)
    return Mixin
