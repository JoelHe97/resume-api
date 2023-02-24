from rest_framework import serializers
from apps.languages.models import Language, LanguageSkill, Level


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class LanguageSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageSkill
        exclude = ["user"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["language"] = instance.language.name
        data["level"] = instance.level.name
        return data
