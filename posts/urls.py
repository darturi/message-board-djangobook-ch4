from django.urls import path  # import path to define urls
from .views import (
    HomePageView,
)  # from our views.py file import the view we built for the homepage

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),  # add the url to the app
]
