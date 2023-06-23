from django.urls import path, include
from .views import (
    WelcomeView,
    AboutMeView,
    SkillView,
    JobExperiencesView,
    CertificatesView,
    SendMailView,
    AzureBlobView,
    ProjectsView,
)

urlpatterns = [
    path("welcome/<str:username>/", WelcomeView.as_view()),
    path("about-me/<str:username>/", AboutMeView.as_view()),
    path("skills/<str:username>/", SkillView.as_view()),
    path("job-experience/<str:username>/", JobExperiencesView.as_view()),
    path("projects/<str:username>/", ProjectsView.as_view()),
    path("certificates/<str:username>/", CertificatesView.as_view()),
    path("send-mail/", SendMailView.as_view()),
    path("azure-blob/", AzureBlobView.as_view()),
]
