# Create your models here.
from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.core.serializers.json import DjangoJSONEncoder

"""
Races and Horses
"""
# Create your models here.


class Race(models.Model):
    date = models.DateField(blank=True)
    year = models.PositiveSmallIntegerField()
    race_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    horses = ArrayField(models.CharField(max_length=200), blank=True)
    TC_PRERACES = 'Pre'
    UPCOMING_TC_RACES = 'TCR'
    PREV_TC = 'PastTCR'
    PAST = 'PastPre'
    CATEGORY_CHOICES = (
        (PAST, "Past Years' Triple Crown Prep Races"),
        (PREV_TC, "Past Years' Triple Crown Races"),
        (UPCOMING_TC_RACES, "This Year's Triple Crown Races"),
        (TC_PRERACES, "Races Leading Up To This Year's Triple Crown"),
    )
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES, blank=True)
    results = JSONField(blank=True)

    class JSONAPIMeta:
        resource_name = 'races'
        JSON_API_PLURALIZE_TYPES = True

    def __str__(self):
        return DjangoJSONEncoder().encode(self)


class Horse(models.Model):
    name = models.CharField(max_length=200, unique=True)
    age = models.PositiveSmallIntegerField()
    owner = models.CharField(max_length=200)
    sire = models.CharField(max_length=200)
    dam = models.CharField(max_length=200)
    career_winnings = models.PositiveIntegerField()
    career_wins = models.PositiveSmallIntegerField()
    career_places = models.PositiveSmallIntegerField()
    career_shows = models.PositiveSmallIntegerField()
    breed = models.CharField(max_length=50)
    races = models.ManyToManyField(Race)

    class JSONAPIMeta:
        resource_name = 'races'
        JSON_API_PLURALIZE_TYPES = True

    def __str__(self):
        return DjangoJSONEncoder().encode(self)
