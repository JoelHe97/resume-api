from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.users.models import User


class JobExperience(models.Model):
    company = models.CharField(
        null=False, blank=False, max_length=50, verbose_name=_("Empresa"))
    description = models.TextField(
        null=True, blank=True, verbose_name=_("Funciones"))
    start_date = models.DateField(
        null=False, blank=False, verbose_name=_("Fecha de inicio"))
    end_date = models.DateField(
        null=True, blank=True, verbose_name=_("Fecha de fin"))
    currently = models.BooleanField(
        default=False, verbose_name=_("Laborando actualmente"))
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Usuario"))

    def __str__(self) -> str:
        return self.company

    class Meta:
        verbose_name = _("Experiencia profesional")
        verbose_name_plural = _("Experiencias profesionales")


class Education(models.Model):
    place = models.CharField(max_length=50, verbose_name=_("Lugar"))
    start_date = models.DateField(
        null=False, blank=False, verbose_name=_("Fecha de inicio"))
    end_date = models.DateField(
        null=False, blank=False, verbose_name=_("Fecha de fin"))
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Usuario"))

    def __str__(self) -> str:
        return self.place

    class Meta:
        verbose_name = _("Centro educativo")
        verbose_name_plural = _("Centros educativos")


class Certificate(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50, verbose_name=_("Nombre"))
    hours = models.SmallIntegerField(
        null=False, blank=False, verbose_name=_("Horas"))
    start_date = models.DateField(
        null=False, blank=False, verbose_name=_("Fecha de inicio"))
    end_date = models.DateField(
        null=False, blank=False, verbose_name=_("Fecha de fin"))
    image = models.ImageField(
        upload_to="certificates/", null=False, blank=False, verbose_name=_("Certificados"))
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Usuario"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Certificado")
        verbose_name_plural = _("Certificados")
