from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from .models import Race, Horse


class RaceResource(resources.ModelResource):
    class Meta:
        model = Race
        skip_unchanged = True
        report_skipped = False


class HorseResource(resources.ModelResource):
    class Meta:
        model = Horse
        skip_unchanged = True
        report_skipped = False


class RaceAdmin(ImportExportActionModelAdmin):
    resource_class = RaceResource


class HorseAdmin(ImportExportActionModelAdmin):
    resource_class = HorseResource


admin.site.register(Race, RaceAdmin, Horse, HorseAdmin)
