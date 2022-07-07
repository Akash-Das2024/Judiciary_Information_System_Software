from itertools import count
from django.contrib import admin
from .models import courtcases,hearing_details

admin.site.register(courtcases)

admin.site.register(hearing_details)


