from rest_framework import serializers
from apps.careers.models import Education, Certificate, JobExperience, Tags
from datetime import date
from utils.images import get_sas


class TagsExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"


class JobExperienceSerializer(serializers.ModelSerializer):
    tags = TagsExperienceSerializer(many=True)

    class Meta:
        model = JobExperience
        exclude = ["user"]

    def difference_dates(self, start_date, end_date):
        difference = end_date - start_date
        years = difference.days // 365
        months = (difference.days % 365) // 30 + 1

        return years, months

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.end_date:
            year, months = self.difference_dates(instance.start_date, instance.end_date)
        else:
            year, months = self.difference_dates(instance.start_date, date.today())

        if year == 1 and months == 0:
            data["months"] = f"1 año"
        elif year == 0:
            data["months"] = f"{months} meses"
        else:
            data["months"] = f"{year} año y {months} meses"
        return data


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        exclude = ["user"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["start_date"] = instance.start_date.strftime("%d-%m-%Y")
        data["end_date"] = instance.end_date.strftime("%d-%m-%Y")
        return data


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        exclude = ["user"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["image"] = get_sas(instance.image.name)
        return data
