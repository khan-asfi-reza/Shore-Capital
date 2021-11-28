from django.db import models


class TimestampAbstract(models.Model):
    # Data Created On
    created_on = models.DateTimeField(auto_now=True)
    # Data Updated On
    updated_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

