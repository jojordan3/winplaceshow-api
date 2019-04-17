# Create your models here.
from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField
from django.core.serializers.json import DjangoJSONEncoder

"""JSON objects
Race object (past years Triple Crown)
{id: ID, year: YEAR, name of race: Name, horses: [list of horse objects]}

Race object (current year)
{id: ID, date: DATE, name of race: NAME, city: CITY, track: track name, horses: [list of horse objects]}

Horse in race object
{id: ID, name: NAME, raceID: RACEID, prize winnings: DOLLARS, rank: RANK}

Prediction JSON object
Horses: {* same as above with probability winning}"""
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

    def __str__(self):
        return DjangoJSONEncoder().encode(self)
