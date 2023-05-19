from rest_framework import generics, views
from apps.users.models import User
from apps.skills.models import Stack, Skill
from .serializers import SkillSerializer


class SkillView(generics.RetrieveAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
