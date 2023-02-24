from django.urls import path, include
from .views import ProfileView

app_name = "users"
urlpatterns = [

    path('<int:pk>/', ProfileView.as_view()),


]
