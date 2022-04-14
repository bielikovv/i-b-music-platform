from django.contrib import admin
from .models import *



class PlaylistsAdmin(admin.ModelAdmin):
    filter_horizontal = ['song']




admin.site.register(Compozition)
admin.site.register(Profile)
admin.site.register(Album)
admin.site.register(Playlists, PlaylistsAdmin)