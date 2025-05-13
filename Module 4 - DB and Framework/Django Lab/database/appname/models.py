from django.db import models


class StudInfo(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.BigIntegerField()
    dob = models.DateField()
    address = models.TextField()

    def __str__(self):
        return self.name
