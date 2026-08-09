from django.contrib.auth.models import User
from import_export import resources
from portal.models import Software

class SofwareResource(resources.ModelResource):
    class Meta:
        model = Software