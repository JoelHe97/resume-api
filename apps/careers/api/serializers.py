from rest_framework import serializers
from apps.careers.models import Education, Certificate, JobExperience


class JobExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobExperience
        exclude = ["user"]


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ["user"]


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        exclude = ["user"]
