from rest_framework import serializers
from apps.skills.models import Skill, Stack
from utils.images import get_sas


class StackSerializer(serializers.Serializer):
    name = serializers.CharField()
    icon = serializers.FileField()

    class Meta:
        model = Stack
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["icon"] = get_sas(instance.icon.name)
        return data


class SkillSerializer(serializers.Serializer):
    percent = serializers.IntegerField()
    stack = StackSerializer()
    id = serializers.IntegerField()

    class Meta:
        model = Skill
        fields = "__all__"
