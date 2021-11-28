from django.core.management.base import BaseCommand, CommandError
from Pages.models.page import Page, PageSection, SectionTextContent, create_underscore_slug


class Command(BaseCommand):
    help = 'Delete All Pages'

    @staticmethod
    def __delete_objects():
        Page.objects.all().delete()
        PageSection.objects.all().delete()
        SectionTextContent.objects.all().delete()

    def handle(self, *args, **options):
        self.__delete_objects()
