from django.db import models

# Create your models here.


class Post(models.Model):  # database model is called 'Post'
    text = models.TextField()  # database will hold data of the type TextField

    def __str__(
        self,
    ):  # a method to return a human readable representation of the model
        return self.text[:50]  # uses / returns first 50 characters of TextField
