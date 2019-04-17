from rest_framework_json_api.serializers import ModelSerializer
from .models import Races

class RaceSerializer(ModelSerializer):
    class Meta:
        model = Races
        fields = ('pk', 'date', 'race_name', 'horses')
        read_only_fields = ('pk', 'date', 'race_name', 'horses')
        many = True

    
class ResultsSerializer(ModelSerializer):
    class Meta:
        model = Races
        fields = ('date', 'race_name', 'results')
        read_only_fields = ('date', 'race_name', 'results')
