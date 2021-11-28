from django.test import TestCase

from Pages.const import DEFAULT_PAGES
from Pages.models.page import Page, PageSection, SectionTextContent
from Pages.utils import create_default_pages


class PageTestCase(TestCase):

    def test_models(self):
        # Test Page Model
        _page = Page.objects.create(name=DEFAULT_PAGES[0])
        self.assertEqual(_page.name, DEFAULT_PAGES[0])
        # Test Section Model
        section = PageSection.objects.create(name=DEFAULT_PAGES[1], slug="page_section", page=_page)
        self.assertEqual(section.page.name, DEFAULT_PAGES[0])
        # Test Content
        content = SectionTextContent.objects.create(name="Text", slug="text", header="Header", section=section)
        self.assertEqual(content.section.name, DEFAULT_PAGES[1])

    def test_default_data(self):
        # Check if default data creation work
        data = create_default_pages()
        self.assertEqual(data, None)
        page = Page.objects.get(name=DEFAULT_PAGES[0])
        self.assertEqual(page.name, DEFAULT_PAGES[0])