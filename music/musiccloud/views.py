from django.contrib.auth import logout, login
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *



def show_main_page(request):
    search_query = request.GET.get('search', '')
    if search_query:
        items = Composition.objects.filter(composition_is_published=True, composition_title__icontains=search_query).order_by('-composition_date')
    else:
        items = Composition.objects.filter(composition_is_published=True).order_by('-composition_date')

    albums = Album.objects.all()
    singers = User.objects.all()
    paginator = Paginator(items, 5)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)
    if request.user.is_authenticated:
        playlist = Playlists.objects.filter(playlist_user=request.user)
        return render(request, 'musiccloud/main_page.html', {'items': items, 'playlist': playlist, 'albums':albums, 'singers':singers, 'page_obj':page_objects})
    return render(request, 'musiccloud/main_page.html', {'items': items, 'albums':albums, 'singers':singers, 'page_obj':page_objects})



def add_to_playlist(request, composition_id, playlist_id):
    playlist = Playlists.objects.get(pk=playlist_id)
    composition = Composition.objects.get(pk=composition_id)
    if request.method == 'POST':
        playlist_cur = playlist.playlist_composition
        playlist_cur.add(composition)
        return redirect(reverse(show_playlist, kwargs={'playlist_id':playlist_id}))
    return render(request, 'musiccloud/composition_to_playlist.html', {'playlist': playlist})



def show_singer_profile(request, singer_id):
    singer_info = User.objects.get(pk=singer_id)
    singer_albums = Album.objects.filter(album_user=singer_id)
    singer_compositions = Composition.objects.filter(composition_user=singer_id, composition_album=None)
    return render(request, 'musiccloud/singer_profile.html', {'singer_info':singer_info, 'singer_albums': singer_albums, 'singer_composition': singer_compositions})



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
        form1 = RedactInfoUserForm(request.POST, request.FILES, instance=request.user)
        form2 = RedactInfoProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            redirect('profile')
    else:
        form1 = RedactInfoUserForm(instance=request.user)
        form2 = RedactInfoProfileForm(instance=request.user.profile)
    return render(request, 'musiccloud/user_profile.html', {'form1':form1, 'form2':form2})



def add_album(request):
    if request.method == 'POST':
        form = AddAlbumForm(request.POST, request.FILES, initial={'album_user': request.user})
        if form.is_valid():
            form.album_user = request.user
            form.save()
    else:
        form = AddAlbumForm(initial={'album_user': request.user})
    return render(request, 'musiccloud/add_album.html', {'form': form})



def show_current_album(request, album_id):
    album = Album.objects.get(pk=album_id)
    compositions = Composition.objects.filter(composition_user=request.user, composition_album=album_id)
    return render(request, 'musiccloud/current_album.html', {'album': album, 'compositions': compositions})



def show_current_composition(request, composition_id):
    compositions = Composition.objects.get(pk=composition_id)
    return render(request, 'musiccloud/current_composition.html', {'compositions': compositions})



def add_compositions_to_album(request, album_title, user_id):
    alb = Album.objects.get(album_title=album_title, album_user=request.user)
    pk = alb.pk
    added_compositions = Composition.objects.filter(composition_album=pk).order_by('-composition_date')

    if request.method == 'POST':
        form = AddAlbumCompositionsForm(request.POST, request.FILES, initial={'composition_album': pk, 'composition_user':request.user, 'composition_singer':request.user.profile, 'composition_envelope': alb.album_envelope, 'composition_is_published': True})
        if form.is_valid():
            form.save()
    else:
        form = AddAlbumCompositionsForm(initial={'composition_album': pk, 'composition_user':request.user, 'composition_singer':request.user.profile, 'composition_envelope': alb.album_envelope, 'composition_is_published':True})
    return render(request, 'musiccloud/composition_to_album.html', {'form': form, 'compositions': added_compositions, 'album':alb})



def show_my_releases(request):
    albums = Album.objects.filter(album_user=request.user)
    compositions = Composition.objects.filter(composition_user=request.user, composition_album=None)
    return render(request, 'musiccloud/my_releases.html', {'albums': albums, 'compositions': compositions})



def confirm_release(request, album_title, user_id):
    alb = Album.objects.get(album_title=album_title, album_user=request.user)
    pk = alb.pk
    added_compositions = Composition.objects.filter(composition_album=pk).order_by('-composition_date')
    if request.method == 'POST':
        album = Album.objects.get(album_title=album_title, album_user=request.user)
        compositions = Composition.objects.filter(composition_album=pk, composition_user=request.user)
        album.album_is_published = True
        album.save()
        for item in compositions:
            item.composition_is_published = True
            item.save()

        return redirect('main_page')
    return render(request, 'musiccloud/confirm_release.html', {'added_comp':added_compositions, 'album':alb})



def add_composition(request):
    if request.method == 'POST':
        form = AddCompositionForm(request.POST, request.FILES, initial={'composition_user': request.user, 'composition_singer': request.user.profile})
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