from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.users.models import User
from ckeditor.fields import RichTextField


class Tags(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Tags profesional")
        verbose_name_plural = _("Tags profesionales")


class JobExperience(models.Model):
    company = models.CharField(
        null=False, blank=False, max_length=50, verbose_name=_("Empresa")
    )
    position = models.CharField(
        null=False, blank=False, max_length=150, verbose_name=_("Posición")
    )
    description = RichTextField()
    start_date = models.DateField(
        null=False, blank=False, verbose_name=_("Fecha de inicio")
    )
    end_date = models.DateField(null=True, blank=True, verbose_name=_("Fecha de fin"))
    currently = models.BooleanField(
        default=False, verbose_name=_("Laborando actualmente")
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name=_("Usuario"),
    )
    tags = models.ManyToManyField(Tags, verbose_name=_("Tags"))

    def __str__(self) -> str:
        return self.company

    class Meta:
        verbose_name = _("Experiencia profesional")
        verbose_name_plural = _("Experiencias profesionales")


class Education(models.Model):
    place = models.CharField(max_length=50, verbose_name=_("Lugar"))
    specialty = models.CharField(max_length=100, verbose_name=_("Especialidad"))
    degree = models.CharField(max_length=100, verbose_name=_("Grado"))
    logo = models.URLField(verbose_name=_("Url"))
    current = models.BooleanField(default=False, verbose_name=_("Empresa actual"))
    start_date = models.DateField(
        null=False, blank=False, verbose_name=_("Fecha de inicio")
    )
    end_date = models.DateField(null=False, blank=False, verbose_name=_("Fecha de fin"))
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name=_("Usuario"),
    )

    def __str__(self) -> str:
        return self.place

    class Meta:
        verbose_name = _("Centro educativo")
        verbose_name_plural = _("Centros educativos")


class Certificate(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50, verbose_name=_("Nombre")
    )
    origin = models.CharField(
        null=False, blank=False, max_length=100, verbose_name=_("Origen")
    )
    hours = models.SmallIntegerField(null=False, blank=False, verbose_name=_("Horas"))
    start_date = models.DateField(
        null=False, blank=False, verbose_name=_("Fecha de inicio")
    )

    end_date = models.DateField(null=False, blank=False, verbose_name=_("Fecha de fin"))
    image = models.ImageField(
        upload_to="certificates/",
        null=False,
        blank=False,
        verbose_name=_("Certificados"),
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name=_("Usuario"),
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Certificado")
        verbose_name_plural = _("Certificados")
