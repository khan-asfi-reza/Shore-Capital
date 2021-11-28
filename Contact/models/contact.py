from django.db import models
from Pages.models import TimestampAbstract


class ContactUsMessage(TimestampAbstract):
    # Sender Name
    name = models.CharField(max_length=300, verbose_name="Name", )
    # Sender Email
    email = models.EmailField(max_length=300, verbose_name="Email")
    # Sender Message
    message = models.TextField(verbose_name="Message")
    # Replied To Message
    replied = models.BooleanField(default=False)
    # Reply Message
    reply = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = "Contact Messages"
        verbose_name_plural = "Contact Messages"
