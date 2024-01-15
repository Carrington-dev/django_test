from django.urls import path
from posts import views

urlpatterns = [
    # path("", views.HomeView.as_view(), name="home")
    path("", views.home, name="home")
]
