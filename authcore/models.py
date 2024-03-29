from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class Hobby(models.Model):
    name = models.CharField(_("название"), max_length=500)

    class Meta:
        verbose_name = _('хобби')
        verbose_name_plural = _('хобби')
        ordering = ['name']


class User(AbstractUser):
    o_name = models.CharField(_("отчество"), max_length=500, blank=True, null=True)
    about = models.TextField(_("обо мне"), blank=True, null=True)
    my_photo = models.ImageField(_("аватар"), upload_to="uploads/photo/", blank=True, null=True)
    gender = models.BooleanField(_("мужчина?"), blank=True, null=True)
    birthday = models.DateField(_("дата рождения"), blank=True, null=True)
    hobby = models.ManyToManyField(Hobby, through='UserHobby', verbose_name=_('хобби'), blank=True)

    class Meta:
        verbose_name = _('пользователь')
        verbose_name_plural = _('пользователи')
        ordering = ['last_name']


class Message(models.Model):
    user_from = models.ForeignKey(
        'user',
        on_delete=models.CASCADE,
        db_column='user_from_id',
        related_name=_('от'))
    user_to = models.ForeignKey(
        'user',
        on_delete=models.CASCADE,
        db_column='user_to_id',
        related_name=_('кому'))
    text = models.TextField(_('сообщение'))
    created = models.DateField(_("дата отправки"), auto_now_add=True)

    class Meta:
        verbose_name = _('сообщение')
        verbose_name_plural = _('сообщения')
        ordering = ['-created']


class Album(models.Model):
    user = models.ForeignKey('user', on_delete=models.CASCADE, db_column='user_id')
    name = models.CharField(_("название"), max_length=500)
    created = models.DateField(_("дата создания"), auto_now_add=True)

    class Meta:
        verbose_name = _('альбом')
        verbose_name_plural = _('альбомы')
        ordering = ['created']


class Photo(models.Model):
    album = models.ForeignKey('album', on_delete=models.CASCADE, db_column='album_id')
    created = models.DateField(_("дата создания"), auto_now_add=True)
    photo = models.ImageField(_("фотография"), upload_to="uploads/photo/")


    class Meta:
        verbose_name = _('фотография')
        verbose_name_plural = _('фотографии')
        ordering = ['-created']


class UserHobby(models.Model):
    user = models.ForeignKey('user', on_delete=models.CASCADE, db_column='user_id')
    hobby = models.ForeignKey('hobby', on_delete=models.CASCADE, db_column='hobby_id')

    class Meta:
        index_together = ['user_id', 'hobby_id']
        verbose_name = _('хобби пользователя')
        verbose_name_plural = _('хобби пользователя')