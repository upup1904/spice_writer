from django.contrib import admin
from liner_note.models import LinerNote, Line


class LinerNoteAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}


class LineAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('episode', 'line', 'text',)}


admin.site.register(LinerNote, LinerNoteAdmin)
admin.site.register(Line, LineAdmin)
