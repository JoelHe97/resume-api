import os

from django.core.cache import cache
from django.core.mail import send_mail
from django.db.models import Prefetch
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_extensions.cache.decorators import cache_response

from apps.careers.api.serializers import (CertificateSerializer,
                                          JobExperienceSerializer)
from apps.careers.models import Certificate, Education, JobExperience
from apps.languages.models import LanguageSkill
from apps.projects.api.serializers import ProjectSerializer
from apps.projects.models import Project
from apps.skills.api.serializers import SkillSerializer
from apps.skills.models import Skill
from apps.users.models import User

from .serializers import AboutMeSerializer, MailSerializer, WelcomeSerializer


class MainView(APIView):
    def get(self, *args, **kwargs):
        return Response({"detail": "Resume on"}, status=status.HTTP_200_OK)


class WelcomeView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = WelcomeSerializer
    lookup_field = "username"
    lookup_url_kwarg = "username"

    def calculate_key(self, view_instance, view_method, request, args, kwargs):
        return "." + "welcome"

    @cache_response(None, key_func="calculate_key")
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


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

    def calculate_key(self, view_instance, view_method, request, args, kwargs):
        return "." + "about"

    @cache_response(None, key_func="calculate_key")
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class SkillView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def calculate_key(self, view_instance, view_method, request, args, kwargs):
        return "." + "skills"

    @cache_response(None, key_func="calculate_key")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class JobExperiencesView(generics.ListAPIView):
    queryset = JobExperience.objects.order_by("start_date")
    serializer_class = JobExperienceSerializer

    def calculate_key(self, view_instance, view_method, request, args, kwargs):
        return "." + "experiences"

    @cache_response(None, key_func="calculate_key")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CertificatesView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def calculate_key(self, view_instance, view_method, request, args, kwargs):
        return "." + "certificates"

    @cache_response(None, key_func="calculate_key")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProjectsView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def calculate_key(self, view_instance, view_method, request, args, kwargs):
        return "." + "projects"

    @cache_response(None, key_func="calculate_key")
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


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


#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             POLLER_WAIT_TIME = 10
#             email = request.data.get("email")
#             message = f'{email} : {request.data.get("message")}'
#             try:
#                 email_client = EmailClient.from_connection_string(
#                     os.environ.get("AZURE_EMAIL_CONNECTION")
#                 )
#                 message = {
#                     "content": {
#                         "subject": "Contacto de mi Web",
#                         "plainText": message,
#                         "html": f"<html><h1>{message}</h1></html>",
#                     },
#                     "recipients": {
#                         "to": [
#                             {
#                                 "address": "huacreenciso97@gmail.com",
#                                 "displayName": "Joel",
#                             }
#                         ]
#                     },
#                     "senderAddress": os.environ.get("AZURE_EMAIL_SENDER"),
#                 }
#                 poller = email_client.begin_send(message)

#                 time_elapsed = 0
#                 while not poller.done():
#                     print("Email send poller status: " + poller.status())

#                     poller.wait(POLLER_WAIT_TIME)
#                     time_elapsed += POLLER_WAIT_TIME

#                     if time_elapsed > 18 * POLLER_WAIT_TIME:
#                         raise RuntimeError("Polling timed out.")

#                 if poller.result()["status"] == "Succeeded":
#                     print(
#                         f"Successfully sent the email (operation id: {poller.result()['id']})"
#                     )
#                 else:
#                     raise RuntimeError(str(poller.result()["error"]))

#             except Exception as ex:
#                 return Response(
#                     {"detail": "ha ocurrido un error"},
#                     status=status.HTTP_400_BAD_REQUEST,
#                 )

#             return Response({"mensaje": "Correo enviado correctamente"})

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AzureBlobView(APIView):
    def post(self, request):
        data = request.data["name"]
        from azure.storage.blob import BlobServiceClient

        blob_service_client = BlobServiceClient.from_connection_string(
            os.environ.get("AZURE_GENERATE_SAS")
        )

        # [START create_sas_token]
        # Create a SAS token to use to authenticate a new client
        from datetime import datetime, timedelta

        from azure.storage.blob import (AccountSasPermissions, ResourceTypes,
                                        generate_account_sas)

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
