from rest_framework import serializers
from apps.users.models import User, Profile
from apps.skills.api.serializers import SkillSerializer
from apps.languages.api.serializers import LanguageSkillSerializer
from apps.careers.api.serializers import JobExperienceSerializer, EducationSerializer, CertificateSerializer


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    skills = SkillSerializer(source='skill_set', many=True)
    languages = LanguageSkillSerializer(source='languageskill_set', many=True)
    job_experience = JobExperienceSerializer(
        source='jobexperience_set', many=True)
    education = EducationSerializer(
        source='education_set', many=True)
    certifications = CertificateSerializer(
        source='certificate_set', many=True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "profile",
                  "skills", "languages", "job_experience", "education", "certifications"]