from django_elasticsearch_dsl import Index, Document
from django_elasticsearch_dsl.registries import registry
from .models import Destination
dests = Index('dests')

@dests.doc_type
class DestinationDocument(Document):
    class Django:
        model = Destination
        fields = [
            'city',
            'country',
            'iso2',
            'iso3',
            'desc',
            'price',
            'img1',
            'img2',
            'img3',
            'img4',
        ]
