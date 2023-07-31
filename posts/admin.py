from django.contrib import admin
from .models import Post  # import the model we created in models.py

# Register your models here.
admin.site.register(Post)  # register the Post model to the admin
