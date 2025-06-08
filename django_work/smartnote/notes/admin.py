from django.contrib import admin
from . import models
# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display = ['title']  # display the title per record in the django admin panel

admin.site.register(models.Notes, NotesAdmin)
