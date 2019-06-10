from django.contrib import admin

# Register your models here.
from .models import Teams,Rankig , Testrankig , Ground , Stats , Runs , Playerstat

admin.site.register(Teams)
admin.site.register(Rankig)
admin.site.register(Testrankig)
admin.site.register(Ground)
admin.site.register(Stats)
admin.site.register(Runs)
admin.site.register(Playerstat)