from grapple.models import GraphQLString
from django_dataslice.models import DataSlice


DataSlice.graphql_fields = [
    GraphQLString("name"),
    GraphQLString("filter"),
]
