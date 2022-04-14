from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=32, label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']



class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=32, label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'password']

class RedactInfoUserForm(forms.ModelForm):
    photo = forms.ImageField(label='Фото', widget=forms.FileInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    nickname = forms.CharField(label='Ник', widget=forms.TextInput(attrs={'class': 'form-control'}))
    about = forms.CharField(label='О себе', widget=forms.Textarea(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    location = forms.CharField(label='Местоположение', widget=forms.TextInput(attrs={'class': 'form-control'}))
    birth_date = forms.DateField(label='Дата рождения', widget=forms.DateInput(attrs={'class': 'form-control'}))
    class Meta:
        model = User
        fields = ['photo', 'first_name', 'last_name', 'nickname', 'email', 'about', 'location', 'birth_date']


class AddPlaylistForm(forms.ModelForm):
    user = forms.ModelChoiceField(label='', empty_label=None, disabled=True, queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    title = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
    envelope = forms.FileField(label='Обложка', widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Playlists
        fields = ['title', 'envelope', 'user']

class AddSongForm(forms.ModelForm):
    user = forms.ModelChoiceField(label='', empty_label=None, disabled=True, queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    title = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
    photo = forms.FileField(label='Обложка', widget=forms.FileInput(attrs={'class': 'form-control'}))
    file = forms.FileField(label='Песня', widget=forms.FileInput(attrs={'class': 'form-control'}))


    class Meta:
        model = Playlists
        fields = ['title', 'envelope', 'user']

class AddAlbumForm(forms.ModelForm):
    title = forms.CharField(label='Название альбома', widget=forms.TextInput(attrs={'class': 'form-control'}))
    envelope = forms.FileField(label='Обложка альбома', widget=forms.FileInput(attrs={'class': 'form-control'}))




class AddCompozitionForm(forms.ModelForm):
    user = forms.ModelChoiceField(label='', empty_label=None, disabled=True, queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    title = forms.CharField(label='Название', widget=forms.TextInput(attrs={'class': 'form-control'}))
    envelope = forms.FileField(label='Обложка', widget=forms.FileInput(attrs={'class': 'form-control'}))
    file = forms.FileField(label='Песня', widget=forms.FileInput(attrs={'class': 'form-control'}))
    singer = forms.ModelChoiceField(label='', empty_label=None, disabled=True, queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Compozition
        fields = ['file', 'title', 'envelope', 'singer', 'user']



