from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=32, label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=32, label='Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']



class RedactInfoUserForm(forms.ModelForm):
    photo = forms.ImageField(label='Photo', widget=forms.FileInput(attrs={'class': 'form-control form-control-sm'}))
    first_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    last_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    nickname = forms.CharField(label='Singer nickname', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    about = forms.CharField(label='About me', widget=forms.Textarea(attrs={'class': 'form-control form-control-sm'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control form-control-sm'}))
    location = forms.CharField(label='My location', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    birth_date = forms.DateField(label='Date of birth', widget=forms.DateInput(attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = User
        fields = ['photo', 'first_name', 'last_name', 'nickname', 'email', 'about', 'location', 'birth_date']



class AddPlaylistForm(forms.ModelForm):
    playlist_user = forms.ModelChoiceField(label='', empty_label=None, disabled=True, queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    playlist_title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    playlist_envelope = forms.FileField(label='Envelope', widget=forms.FileInput(attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = Playlists
        fields = ['playlist_title', 'playlist_envelope', 'playlist_user']



class AddAlbumForm(forms.ModelForm):
    album_title = forms.CharField(label='Album name', widget=forms.TextInput(attrs={'class': 'form-control '}))
    album_envelope = forms.FileField(label='Album envelope', widget=forms.FileInput(attrs={'class': 'form-control'}))
    album_user = forms.ModelChoiceField(label='', empty_label=None, queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = Album
        fields = ['album_title', 'album_envelope', 'album_user']



class AddAlbumCompositionsForm(forms.ModelForm):
    composition_title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    composition_file = forms.FileField(label='Song file', widget=forms.FileInput(attrs={'class': 'form-control form-control-sm', 'multiple': True}))
    composition_envelope = forms.FileField(label='Envelope', widget=forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm'}))
    composition_album = forms.ModelChoiceField(label='', empty_label=None, queryset=Album.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    composition_user = forms.ModelChoiceField(label='', empty_label=None, queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    composition_singer = forms.ModelChoiceField(label='', empty_label=None, queryset=Profile.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))

    class Meta:
        model = Composition
        fields = ('composition_title', 'composition_file', 'composition_envelope', 'composition_album', 'composition_user', 'composition_singer')



class AddCompositionForm(forms.ModelForm):
    composition_user = forms.ModelChoiceField(label='', empty_label=None, queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    composition_title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'}))
    composition_envelope = forms.FileField(label='Envelope', widget=forms.ClearableFileInput(attrs={'class': 'form-control form-control-sm'}))
    composition_file = forms.FileField(label='Song file', widget=forms.FileInput(attrs={'class': 'form-control form-control-sm'}))
    composition_singer = forms.ModelChoiceField(label='', empty_label=None, queryset=Profile.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))
    composition_is_published = forms.BooleanField(label='Release', initial=True, required=False)

    class Meta:
        model = Composition
        fields = ['composition_file', 'composition_title', 'composition_envelope', 'composition_singer', 'composition_user', 'composition_is_published']

class AddCompToPlaylistForm(forms.ModelForm):
    playlist_composition = forms.ModelChoiceField(label='Плейлист:', empty_label=None, queryset=Playlists.objects.all(), widget=forms.Select(attrs={'class': 'form-control form-control-sm'}))

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('playlist_user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['playlist_composition'].queryset = Playlists.objects.filter(playlist_user=user)

    class Meta:
        model = Composition
        fields = ['playlist_composition', ]





