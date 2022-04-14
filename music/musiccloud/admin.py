from django.contrib import admin
from .models import *



class PlaylistsAdmin(admin.ModelAdmin):
    filter_horizontal = ['playlist_composition']




admin.site.register(Composition)
admin.site.register(Profile)
admin.site.register(Album)
admin.site.register(Playlists, PlaylistsAdmin)