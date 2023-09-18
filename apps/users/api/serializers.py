from rest_framework import serializers
from apps.users.models import User, Profile
from apps.skills.api.serializers import SkillSerializer
from apps.languages.api.serializers import LanguageSkillSerializer
from apps.careers.api.serializers import (
    JobExperienceSerializer,
    EducationSerializer,
    CertificateSerializer,
)
import os
from datetime import date
from apps.careers.api.serializers import EducationSerializer
from apps.languages.api.serializers import LanguageSkillSerializer
from utils.images import get_sas


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        today = date.today()
        birth_year = instance.birth_date.year
        birth_month = instance.birth_date.month
        birth_day = instance.birth_date.day
        data["district"] = instance.district.name
        data["province"] = instance.district.province.name
        data["department"] = instance.district.province.department.name
        data["age"] = (
            today.year
            - birth_year
            - ((today.month, today.day) < (birth_month, birth_day))
        )
        return data

    # def to_representation(self, instance):
    #     data= super().to_representation(instance)
    #     return data


class WelcomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["description"] = instance.profile.description
        data["cv"] = instance.profile.cv.url if instance.profile.cv else None
        data["short_description"] = instance.profile.short_description
        data["whatsapp"] = instance.profile.whatsapp
        data["github"] = instance.profile.github
        data["linkedin"] = instance.profile.linkedin
        data["linkedin"] = instance.profile.linkedin
        return data


class AboutMeSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    education = EducationSerializer(many=True, source="education_set")
    idioms = LanguageSkillSerializer(many=True, source="languageskill_set")

    class Meta:
        model = User
        fields = ["first_name", "last_name", "profile", "education", "idioms"]


class MailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    message = serializers.CharField(required=True)
