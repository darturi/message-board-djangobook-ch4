from django.shortcuts import render
from django.views.generic import ListView  # import the generic view template
from .models import Post  # from our models file import the Post model


# Create your views here.


class HomePageView(ListView):  # create a new view for the Home Page
    model = Post  # assign the model Post
    template_name = "home.html"  # assign the template home.html

    # Note: this is a subclass and so model and template_name are class variables of the superclass
