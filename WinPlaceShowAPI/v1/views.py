from rest_framework_json_api.generics import GenericAPIView
from rest_framework_json_api.renderers import JSONRenderer
from WinPlaceShowAPI.v1.serializers import RaceSerializer, ResultsSerializer
from .models import Races


HTTP_422_UNPROCESSABLE_ENTITY = 422

# Create your views here.
class PrevTCView(GenericAPIView):
    """
    API endpoint for previous years' Triple Crown Results
    """
    queryset = Races.objects.filter(category='PTC')
    serializer_class = RaceSerializer




class PrevPreView(GenericAPIView):
    """
    API endpoint for this year's pre-races or qualifying races
    """
    lookup_url_kwarg = horse
    lookup_field = horses
    queryset = Races.objects.filter(category='PTS', horses__contains=horse)
    serializer_class = RaceSerializer



class UpcomingTCView(GenericAPIView):
    """
    API endpoint for this year's qualifying races
    """
    queryset = Races.objects.filter(category='TCR')
    serializer_class = RaceSerializer


class GetResultsView(GenericAPIView):
    """
    API endpoint for results of completed races
    """
    lookup_url_kwarg = race_id
    serializer_class = ResultsSerializer
    queryset = Races.objects.get(pk=race_id)


class PredictResultsView(GenericAPIView):
    """
    API endpoint for results of completed races
    """
    lookup_url_kwarg = race_id
    serializer_class = ResultsSerializer
    queryset = Races.objects.get(pk=race_id)
