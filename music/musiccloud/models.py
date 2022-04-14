from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Пользователь')
    envelope = models.ImageField(verbose_name='Обложка', upload_to='photo/%Y/%m/%d')
    title = models.CharField(max_length=128, verbose_name='Название альбома', default='Без названия', blank=True)
    date_album = models.DateField(auto_now_add=True, verbose_name='Дата релиза альбома')

    def __str__(self):
        return self.title


class Playlists(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь', null=True)
    title = models.CharField(max_length=128, verbose_name='Название Плейлиста')
    envelope = models.ImageField(verbose_name='Обложка плейлиста', upload_to='photo/%Y/%m/%d')
    date_playlist = models.DateField(auto_now_add=True, verbose_name='Дата создания плейлиста')
    song = models.ManyToManyField('Compozition', verbose_name='Песня', blank=True)

    def __str__(self):
        return self.title



class Compozition(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.PROTECT, null=True)
    envelope = models.ImageField(verbose_name='Обложка', upload_to='photo/%Y/%m/%d', blank=True, null=True)
    title = models.CharField(max_length=455, verbose_name='Название', default='Без названия', blank=True)
    file = models.FileField(verbose_name='Песня', upload_to='audio')
    album = models.ForeignKey(Album, verbose_name='Альбом', blank=True, on_delete=models.CASCADE, null=True)
    date_song = models.DateField(auto_now_add=True, verbose_name='Дата релиза песни', null=True)
    singer = models.ForeignKey('Profile', on_delete=models.PROTECT, null=True, verbose_name='Исполнитель')

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Имя пользователя")
    photo = models.ImageField(verbose_name='Фото', upload_to='photo/%Y/%m/%d', blank=True)
    location = models.CharField(verbose_name="Местоположение", max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    about = models.TextField(blank=True, verbose_name="О себе")
    nickname = models.CharField(max_length=128, verbose_name="Исполнитель", null=True)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
