from django.db import models

# Create your models here.

class Member(models.Model):
    DEFAULT_PK=1
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)

    def __str__(self):
        return self.firstname + " " + self.lastname
