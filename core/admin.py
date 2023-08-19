from django.contrib import admin
from . import models 
# Register your models here.

admin.site.register(models.Profile)
admin.site.register(models.Education)
admin.site.register(models.Experience)
admin.site.register(models.Service)
admin.site.register(models.Project)
admin.site.register(models.Contact)