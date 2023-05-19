from django.urls import path, include
from .views import SkillView

app_name = "users"
urlpatterns = [
    path("<int:pk>/", SkillView.as_view()),
]
