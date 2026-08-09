from django.contrib import admin
from portal.models import Software
from import_export.admin import ImportExportModelAdmin

# class SoftwareAdmin(admin.ModelAdmin):
class SoftwareAdmin(ImportExportModelAdmin):
    list_display=('id','nivel','nombre','define')
    ordering=('-nivel','nombre')
    search_fields = ('nombre','define')
    list_display=('id','nivel','nombre','define')
    list_display_links=('nombre',)
    # list_editable=('nombre','define')
    list_filter=('nivel',)
    list_per_page = 4

# Register your models here.
admin.site.register(Software, SoftwareAdmin)
admin.site.site_header = "Tecnológico Nacional de México"
admin.site.index_title = "Tecnologías Python"
admin.site.site_title = "TecNM"