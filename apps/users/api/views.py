from rest_framework import generics, views
from apps.users.models import User
from apps.skills.models import Skill
from apps.skills.api.serializers import SkillSerializer
from apps.careers.models import JobExperience, Certificate
from apps.careers.api.serializers import JobExperienceSerializer, CertificateSerializer
from .serializers import WelcomeSerializer, AboutMeSerializer, MailSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail
from rest_framework import status
from azure.storage.blob import BlobServiceClient
import os
from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta
from django.db.models import Prefetch
from apps.careers.models import Education
from apps.languages.models import LanguageSkill


class MainView(APIView):
    def get(self, *args, **kwargs):
        return Response({"detail": "Resume on"}, status=status.HTTP_200_OK)


class WelcomeView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = WelcomeSerializer
    lookup_field = "username"
    lookup_url_kwarg = "username"


class AboutMeView(generics.RetrieveAPIView):
    queryset = User.objects.select_related(
        "profile", "profile__district"
    ).prefetch_related(
        Prefetch("education_set", queryset=Education.objects.select_related("user")),
        Prefetch(
            "languageskill_set",
            queryset=LanguageSkill.objects.select_related("user", "language", "level"),
        ),
    )
    serializer_class = AboutMeSerializer
    lookup_field = "username"
    lookup_url_kwarg = "username"


class SkillView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user__username=self.kwargs["username"])


class JobExperiencesView(generics.ListAPIView):
    queryset = JobExperience.objects.all()
    serializer_class = JobExperienceSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user__username=self.kwargs["username"])


class CertificatesView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def get_queryset(self):
        return super().get_queryset().filter(user__username=self.kwargs["username"])


class SendMailView(APIView):
    serializer_class = MailSerializer

    def post(self, request):
        serializer = MailSerializer(data=request.data)

        if serializer.is_valid():
            subject = "Contacto de mi Web"
            email = request.data.get("email")
            message = f'{email} : {request.data.get("message")}'

            send_mail(
                subject,
                message,
                email,
                ["huacreenciso97@gmail.com"],
                fail_silently=False,
            )

            return Response({"mensaje": "Correo enviado correctamente"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AzureBlobView(APIView):
    def post(self, request):
        data = request.data["name"]
        AZURE_ACC_NAME = os.environ.get("AZURE_ACCOUNT_NAME")
        AZURE_PRIMARY_KEY = os.environ.get("AZURE_ACCOUNT_KEY")
        AZURE_CONTAINER = os.environ.get("AZURE_CONTAINER")
        AZURE_BLOB = data
        from azure.storage.blob import BlobServiceClient

        blob_service_client = BlobServiceClient.from_connection_string(
            "DefaultEndpointsProtocol=https;AccountName=resumebucket;AccountKey=61QyF+BPJXmiDKjP1IFAn8bCJSjcm5ndSnq9py9QMXX7HeoDo2KyLKd5Own2P/0ES5+iVWwI44DN+AStdHGFww==;EndpointSuffix=core.windows.net"
        )

        # [START create_sas_token]
        # Create a SAS token to use to authenticate a new client
        from datetime import datetime, timedelta
        from azure.storage.blob import (
            ResourceTypes,
            AccountSasPermissions,
            generate_account_sas,
        )

        sas_token = generate_account_sas(
            blob_service_client.account_name,
            account_key=blob_service_client.credential.account_key,
            resource_types=ResourceTypes(object=True),
            permission=AccountSasPermissions(read=True),
            expiry=datetime.utcnow() + timedelta(hours=1),
        )
        # print sas_url
        # print 'https://'+AZURE_ACC_NAME+'.blob.core.windows.net/'+AZURE_CONTAINER+'/'+AZURE_BLOB+'?'+sas_url
        # sas = generate_blob_sas(account_name=os.environ.get("AZURE_ACCOUNT_NAME"),
        #                     account_key=os.environ.get("AZURE_ACCOUNT_KEY"),
        #                     container_name=os.environ.get("AZURE_CONTAINER"),
        #                     blob_name=data,
        #                     permission=BlobSasPermissions(read=True),
        #                     expiry=datetime.utcnow() + timedelta(hours=2))

        # # logging.info('https://'+AZURE_ACC_NAME+'.blob.core.windows.net/'+AZURE_CONTAINER+'/'+file_name+'?'+sas)
        sas_url = (
            "https://"
            + os.environ.get("AZURE_ACCOUNT_NAME")
            + ".blob.core.windows.net/"
            + os.environ.get("AZURE_CONTAINER")
            + "/"
            + data
            + "?"
            + sas_token
        )
        # # return sas_url
        return Response({"image": sas_url}, status=status.HTTP_200_OK)
