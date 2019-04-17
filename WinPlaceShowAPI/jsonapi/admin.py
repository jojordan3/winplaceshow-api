from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from .models import Races


class RacesResource(resources.ModelResource):
    class Meta:
        model = Races
        skip_unchanged = True
        report_skipped = False


class RacesAdmin(ImportExportActionModelAdmin):
    resource_class = RacesResource


admin.site.register(Races, RacesAdmin)
