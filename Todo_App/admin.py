from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display= ('TaskName','isCompleted','updated_at')
    search_fields = ('TaskName',)

admin.site.register(Task,TaskAdmin)
