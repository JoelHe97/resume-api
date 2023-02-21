from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.users.models import User


class Language(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50, verbose_name=_("Nombre"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Lenguaje")
        verbose_name_plural = _("Lenguajes")


class Level(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50, verbose_name=_("Nombre"))
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Lenguaje"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Nivel")
        verbose_name_plural = _("Niveles")


class LanguageSkill(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Usuario"))
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Lenguaje"))
    level = models.ForeignKey(
        Level, on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Nivel"))

    def __str__(self) -> str:
        return self.user.username + " " + self.language.name

    class Meta:
        verbose_name = _("Idioma")
        verbose_name_plural = _("Idiomas")
