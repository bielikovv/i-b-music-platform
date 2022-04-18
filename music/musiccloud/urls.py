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
    path('add-release/album/', add_album, name="add-album"),
    path('add-release/composition/', add_composition, name="composition"),
    path('profile/', show_user_form, name="profile"),
    path('add-release/album/albcompadd/<str:album_title>/', add_compositions_to_album, name="albcompadd"),
    path('add-release/album/albcompadd/<str:album_title>/confirm-release/', confirm_release, name="confirm_release"),
    path('my-releases/', show_my_releases, name="my_releases"),
    path('my-releases/album/<int:album_id>/', show_current_album, name="current-album"),
    path('my-releases/composition/<int:composition_id>/', show_current_composition, name="current-composition"),


]