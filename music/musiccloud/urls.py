from django.urls import path
from .views import *

urlpatterns = [
    path('', show_main_page, name="main_page"),
    path('register/', register, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),
    path('myplaylists/', show_mp3, name="mp3"),
    path('myplaylists/playlist/<int:playlist_id>/', show_playlist, name="current_playlist"),
    path('add-release/', add_release, name="add-release"),
    path('add-relize/album', add_album, name="add-album"),
    path('add-relize/composition', add_composition, name="composition"),
    path('profile', show_user_form, name="profile"),


]