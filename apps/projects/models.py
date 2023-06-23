from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.users.models import User
from apps.careers.models import Tags


class Project(models.Model):
    description = models.TextField(
        null=False, blank=False, verbose_name=_("Descripción")
    )
    url = models.URLField(null=True, blank=True)
    tags = models.ManyToManyField(Tags, verbose_name=_("Tags"))
    image = models.ImageField(
        upload_to="projects", null=True, blank=True, verbose_name=_("Projecto")
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("Usuario")
    )

    def __str__(self) -> str:
        return self.url

    class Meta:
        verbose_name = _("Proyecto")
        verbose_name_plural = _("Proyectos")
