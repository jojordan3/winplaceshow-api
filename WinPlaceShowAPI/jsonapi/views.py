import re
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.serializers import Serializer
from .predictions import RacePredictor
from .models import Race, Horse


slug_stuff = re.compile(r'[_\-]+')
def de_sluggify(some_string, slugs_=slug_stuff):
    new_string = some_string.replace(slug_stuff, ' ')
    return new_string


# Create your views here.
@api_view(exclude_from_schema=['results'])
def category(request, cat=None):
    try:
        assert (cat in Race.CATEGORY_CHOICES)
    except:
        raise Http404("Whoops... Try again")
    else:
        queryset = Race.objects.filter(category=cat)
        serializer= Serializer(queryset, many=True)
        return Response(serializer.data)


@api_view(exclude_from_schema=['results'])
def horseview(request, horsename=None):
    try:
        horse_ = de_sluggify(horsename)
        queryset = Horse.objects.filter(horses__contains=[horse_])
        serializer = Serializer(queryset, many=True)
        return Response(serializer.data)
    except:
        raise Http404("Whoops... Try again")


@api_view(exclude_from_schema=['horses'])
def results(request, pk=None):
    try:
        race = get_object_or_404(Race.objects.all(), pk=pk)
        assert (race['category'] in ['Pre', 'Past'])
    except:
        raise Http404("We don't have results for that race")

    serializer = Serializer(race, many=False)
    return Response(serializer.data)


@api_view()
def predict_results(request, pk=None):
    race = get_object_or_404(Horse.objects.filter(category='TCR', pk=pk))
    try:
        race.results = RacePredictor(race.horses)
        serializer = Serializer(race, many=False)
    except:
        raise Http404("Whoops... try again")
    return Response(serializer)
