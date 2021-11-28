from django.core.management.base import BaseCommand, CommandError
from fontawesome_5 import Icon

from Pages.models.page import Page, PageSection, SectionTextContent, create_underscore_slug, PageComponent
from Pages.const import PAGES, CLASS_PAGE_COMPONENTS
from Pages.utils import create_default_pages


class Command(BaseCommand):
    help = 'Create Default Pages'

    @staticmethod
    def __delete_objects():
        Page.objects.all().delete()
        PageSection.objects.all().delete()
        SectionTextContent.objects.all().delete()
        PageComponent.objects.all().delete()

    def handle(self, *args, **options):
        self.__delete_objects()
        create_default_pages()
        self.stdout.write(self.style.SUCCESS('Successfully Created DEFAULT Pages'))