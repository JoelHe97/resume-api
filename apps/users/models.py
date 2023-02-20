from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.locations.models import District


class Profile(models.Model):
    description = models.TextField(
        null=True, blank=True, verbose_name=_("Descripcion"))
    short_description = models.CharField(
        max_length=50, null=True, blank=True, verbose_name=_("Descripcion corta"))
    photo = models.ImageField(
        upload_to="photos", null=True, blank=True, verbose_name=_("Foto"))
    birth_date = models.DateField(
        null=False, blank=False, verbose_name=_("Fecha de nacimiento"))
    phone = models.CharField(
        max_length=9, null=False, blank=False, verbose_name=_("Celular"))
    email = models.EmailField(null=False, blank=False, verbose_name=_("Email"))
    address = models.TextField(
        null=False, blank=False, verbose_name=_("Dirección"))
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Distrito"))
    country = models.CharField(
        max_length=50, null=False, blank=False, verbose_name=_("País"))
    linkedin = models.URLField(
        null=False, blank=False, verbose_name=("Linkedin"))
    github = models.URLField(null=False, blank=False, verbose_name=("Github"))

    class Meta:
        verbose_name = _("Perfil")
        verbose_name_plural = _("Perfiles")


class User(AbstractUser):
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Perfil")
    )

    class Meta:
        verbose_name = _("Usuario")
        verbose_name_plural = _("Usuarios")
