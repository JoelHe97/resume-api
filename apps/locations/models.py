from django.db import models
from django.utils.translation import gettext_lazy as _


class Department(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False, verbose_name=_("Nombre"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Departamento")
        verbose_name_plural = _("Departamentos")


class Province(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False, verbose_name=_("Nombre"))
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Departamento"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Provincia")
        verbose_name_plural = _("Provincias")


class District(models.Model):
    name = models.CharField(
        max_length=50, null=False, blank=False, verbose_name=_("Nombre"))
    province = models.ForeignKey(
        Province, on_delete=models.CASCADE, null=False, blank=False, verbose_name=_("Provincia"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = _("Distrito")
        verbose_name_plural = _("Distritos")
