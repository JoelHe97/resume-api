from rest_framework import serializers
from apps.skills.models import Skill, Stack


class StackSerializer(serializers.Serializer):
    name = serializers.CharField()
    icon = serializers.URLField()

    class Meta:
        model = Stack
        fields = "__all__"


class SkillSerializer(serializers.Serializer):
    percent = serializers.IntegerField()
    stack = StackSerializer()

    class Meta:
        model = Skill
        fields = ["percent"]
