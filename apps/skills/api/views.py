from rest_framework import generics, views
from apps.users.models import User
from apps.skills.models import Stack, Skill
from .serializers import SkillSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class SkillView(generics.RetrieveAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    @method_decorator(cache_page(None, key_prefix="skill"))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
