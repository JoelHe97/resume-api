from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.users.models import User


class Stack(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Nombre"))
    icon = models.ImageField(
        upload_to="icon", null=True, blank=True, verbose_name=_("Icono"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Stack")
        verbose_name_plural = _("Stacks")


class Skill(models.Model):
    stack = models.ForeignKey(Stack, on_delete=models.CASCADE,
                              null=True, blank=True, verbose_name=_("Stack"))
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True, verbose_name=_("Usuario"))
    percent = models.IntegerField(
        null=False, blank=False, verbose_name=_("POrcentaje de conocimiento"))

    def __str__(self) -> str:
        return f'{self.user}-{self.stack}'

    class Meta:
        verbose_name = _("Habilidad")
        verbose_name_plural = _("Habilidades")
