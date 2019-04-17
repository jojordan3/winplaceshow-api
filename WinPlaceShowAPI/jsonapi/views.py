from .serializers import RaceSerializer, ResultsSerializer
from .models import Races
from .routers import CustomReadOnlyRouter
from drja import filters
from drja import django_filters
from rest_framework import SearchFilter, mixins
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

HTTP_422_UNPROCESSABLE_ENTITY = 422

# Create your views here.
class PastViewSet(ReadOnlyModelViewSet):
    """
    API endpoint for previous years' Triple Crown Results
    """
    resource_name = 'races'
    queryset = Races.objects.filter(category='Past')
    serializer_class = RaceSerializer

class PreViewSet(mixins.RetrieveModelMixin, GenericViewSet):
    """
    API endpoint for this year's pre-races or qualifying races
    """
    resource_name = 'races'
    lookup_field = 'horses'
    queryset = Races.objects.filter(category='Pre')
    serializer_class = RaceSerializer


class TCRViewSet(ReadOnlyModelViewSet):
    """
    API endpoint for this year's qualifying races
    """
    resource_name = 'races'
    queryset = Races.objects.filter(category='TCR')
    serializer_class = RaceSerializer


class ResultsView(ReadOnlyModelViewSet):
    """
    API endpoint for results of completed races
    """
    resource_name = 'races'
    lookup_url_kwarg = race_id
    serializer_class = ResultsSerializer
    queryset = Races.objects.get(pk=race_id)


class PredictResultsView(ReadOnlyModelViewSet):
    """
    API endpoint for results of completed races
    """
    resource_name = 'races'
    lookup_url_kwarg = race_id
    serializer_class = ResultsSerializer
    queryset = Races.objects.get(pk=race_id)
