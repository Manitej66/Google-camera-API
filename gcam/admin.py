from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Gcam
# Register your models here.


@admin.register(Gcam)
class GcamAdmin(ImportExportModelAdmin):
    pass
