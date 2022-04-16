from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q

def show_main_page(request):
    items = Composition.objects.all()
    playlist = Playlists.objects.filter(playlist_user=request.user)
    # if request.method == 'POST':
    #     form = AddCompToPlaylistForm(request.POST, playlist_user=request.user)
    #     if form.is_valid():
    #         pass
    # else:
    #     form = AddCompToPlaylistForm(playlist_user=request.user)
    return render(request, 'musiccloud/main_page.html', {'items': items, 'playlist':playlist})



def show_mp3(request):
    track = Playlists.objects.filter(playlist_user=request.user)
    if request.method == 'POST':
        form = AddPlaylistForm(request.POST, request.FILES, initial={'playlist_user': request.user})
        if form.is_valid():
            form.save()
            return redirect('mp3')
    else:
        form = AddPlaylistForm(initial={'playlist_user': request.user})
    return render(request, 'musiccloud/mp3_player.html', {'track': track, 'form':form})



def show_playlist(request, playlist_id):
    playlist = Playlists.objects.get(pk=playlist_id)
    compositions = playlist.playlist_composition.all()
    return render(request, 'musiccloud/current_playlist.html', {'playlist':playlist, 'compositions':compositions})



def show_user_form(request):
    if request.method == 'POST':
        form = RedactInfoUserForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            redirect('profile')
    else:
        form = RedactInfoUserForm(instance=request.user.profile, initial={'first_name':request.user.first_name, 'last_name':request.user.last_name, 'email':request.user.email })
    return render(request, 'musiccloud/user_profile.html', {'form':form})



def add_album(requset):
    return render(requset, 'musiccloud/add_album.html')



def add_composition(request):
    if request.method == 'POST':
        form = AddCompositionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = AddCompositionForm(initial={'composition_user': request.user, 'composition_singer': request.user.profile})
    return render(request, 'musiccloud/add_compozition.html', {'form': form})



def add_release(request):
    return render(request, 'musiccloud/add_release.html')



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_page')
    else:
        form = RegisterForm()
    return render(request, 'musiccloud/register.html', {'form':form})



def login_user(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_page')
    else:
        form = LoginForm()
    return render(request, 'musiccloud/login.html', {"form": form})



def logout_user(request):
    logout(request)
    return redirect('main_page')