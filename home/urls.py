from django.urls import path
from home.views import views

urlpatterns = [
    path("", views.home, name="home"),
]
