# Create your models here.
from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.core.serializers.json import DjangoJSONEncoder

"""
Races and Horses
"""
# Create your models here.

class Races(models.Model):
    date = models.DateField()
    race_name = models.CharField(max_length=200)
    horses = ArrayField(models.CharField(max_length=200))
    TC_PRERACES = 'Pre'
    UPCOMING_TC_RACES = 'TCR'
    PREV_TC = 'Past'
    CATEGORY_CHOICES = (
        (PREV_TC, "Past Years' Triple Crown Races"),
        (UPCOMING_TC_RACES, "This Year's Triple Crown Races"),
        (TC_PRERACES, "Races Leading Up To This Year's Triple Crown")
    )
    category = models.CharField(max_length=4, choices=CATEGORY_CHOICES)
    results = JSONField()

    class JSONAPIMeta:
        resource_name = 'races'
        JSON_API_PLURALIZE_TYPES = True

    def __str__(self):
        return DjangoJSONEncoder().encode(self)


class Horses(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveSmallIntegerField()
    owner = models.CharField(max_length=200)
    sire = models.CharField(max_length=200)
    dam = models.CharField(max_length=200)
    career_winnings = models.PositiveIntegerField()
    career_wins = models.PositiveSmallIntegerField()
    career_places = models.PositiveSmallIntegerField()
    career_shows = models.PositiveSmallIntegerField()
    breed = models.CharField(max_length=50)

    class JSONAPIMeta:
        resource_name = 'races'
        JSON_API_PLURALIZE_TYPES = True

    def __str__(self):
        return DjangoJSONEncoder().encode(self)
