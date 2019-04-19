from django.urls import re_path, path
from .jsonapi.views import *
from django.contrib import admin

"""Search by criteria: 
Past Triple Crown Races Past: Immediately List All Races (No search criteria)
This year's past races: Horse Name
Future Race: Immediately List All Races (No search criteria)

JSON objects
Race object (past years Triple Crown)
{id: ID, year: YEAR, name of race: Name, horses: [list of horse objects]}

Race object (current year)
{id: ID, date: DATE, name of race: NAME, city: CITY, track: track name, horses: [list of horse objects]}

Horse in race object
{id: ID, name: NAME, raceID: RACEID, prize winnings: DOLLARS, rank: RANK}

Prediction JSON object
Horses: {* same as above with probability winning}
"""



urlpatterns = [
    re_path(r"(races/)(?P<cat>(Pre|Past|TCR))/", category),
    path("horse/<slug:horsename>/", horseview),
    path("results/<int:pk>/", results),
    path("predict/<int:pk>", predict_results),
    path("admin/", admin.site.urls, name="admin"),
]

