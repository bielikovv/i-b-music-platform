from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Album(models.Model):
    album_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='Username')
    album_envelope = models.ImageField(verbose_name='Envelope', upload_to='photo/%Y/%m/%d', null=True)
    album_title = models.CharField(max_length=128, verbose_name='Title', default='NoName', blank=True)
    date_album = models.DateField(auto_now_add=True, verbose_name='Album release date')

    def __str__(self):
        return self.album_title



class Playlists(models.Model):
    playlist_user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Username', null=True)
    playlist_title = models.CharField(max_length=128, verbose_name='Title', null=True)
    playlist_envelope = models.ImageField(verbose_name='Envelope', upload_to='photo/%Y/%m/%d', null=True)
    date_playlist = models.DateField(auto_now_add=True, verbose_name='Playlist creation date')
    playlist_composition = models.ManyToManyField('Composition', verbose_name='Composition', blank=True)

    def __str__(self):
        return self.playlist_title



class Composition(models.Model):
    composition_user = models.ForeignKey(User, verbose_name='Username', on_delete=models.PROTECT, null=True)
    composition_envelope = models.ImageField(verbose_name='Envelope', upload_to='photo/%Y/%m/%d', blank=True, null=True)
    composition_title = models.CharField(max_length=455, verbose_name='Title', default='NoName', blank=True)
    composition_file = models.FileField(verbose_name='Composition file', upload_to='audio')
    composition_album = models.ForeignKey(Album, verbose_name='Album', blank=True, on_delete=models.CASCADE, null=True)
    composition_date = models.DateField(auto_now_add=True, verbose_name='Song release date', null=True)
    composition_singer = models.ForeignKey('Profile', on_delete=models.PROTECT, null=True, verbose_name='Singer')

    def __str__(self):
        return self.composition_title



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Username")
    photo = models.ImageField(verbose_name='Photo', upload_to='photo/%Y/%m/%d', blank=True)
    location = models.CharField(verbose_name="Location", max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True, verbose_name="Date of birth")
    about = models.TextField(blank=True, verbose_name="About")
    nickname = models.CharField(max_length=128, verbose_name="Singer nickname", null=True)



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
