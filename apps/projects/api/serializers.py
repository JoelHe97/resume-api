from apps.projects.models import Project
from rest_framework import serializers
from utils.images import get_sas
from apps.careers.api.serializers import TagsExperienceSerializer


class ProjectSerializer(serializers.ModelSerializer):
    tags = TagsExperienceSerializer(many=True)

    class Meta:
        model = Project
        exclude = ["user"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["image"] = get_sas(instance.image.name)
        return data
