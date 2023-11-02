from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache
from apps.users.models import Profile
from apps.skills.models import Skill, Stack
from apps.careers.models import JobExperience, Certificate, Education, Tags
from apps.languages.models import LanguageSkill, Level, Language
from apps.projects.models import Project


@receiver(post_save, sender=Profile)
def invalidate_cache(sender, instance, **kwargs):
    cache.delete_pattern("*welcome*")
    cache.delete_pattern("*about*")


@receiver(post_save, sender=Skill)
def invalidate_cache(sender, instance, **kwargs):
    cache.delete_pattern("*skill*")


@receiver(post_save, sender=Stack)
def invalidate_cache(sender, instance, **kwargs):
    cache.delete_pattern("*skill*")


@receiver(post_save, sender=Stack)
def invalidate_cache(sender, instance, **kwargs):
    cache.delete_pattern("*skills*")


@receiver(post_save, sender=JobExperience)
def invalidate_cache(sender, instance, **kwargs):
    cache.delete_pattern("*experiences*")


@receiver(post_save, sender=Certificate)
def invalidate_cache(sender, instance, **kwargs):
    cache.delete_pattern("*certificates*")


@receiver(post_save, sender=Education)
def invalidate_cache(sender, instance, **kwargs):
    cache.delete_pattern("*about*")


@receiver(post_save, sender=LanguageSkill)
def invalidate_cache(sender, instance, **kwargs):
    cache.delete_pattern("*about*")


@receiver(post_save, sender=Level)
def invalidate_cache(sender, instance, **kwargs):
    cache.delete_pattern("*about*")


@receiver(post_save, sender=Language)
def invalidate_cache(sender, instance, **kwargs):
    cache.delete_pattern("*about*")


@receiver(post_save, sender=Project)
def invalidate_cache(sender, instance, **kwargs):
    cache.delete_pattern("*projects*")


@receiver(post_save, sender=Tags)
def invalidate_cache(sender, instance, **kwargs):
    cache.delete_pattern("*experiences*")
