from django.db import models
from django.utils.safestring import mark_safe
from fontawesome_5.fields import IconField
from django.core.files import File

from Pages.model_utils import compress_image
from Pages.models import TimestampAbstract


def create_underscore_slug(instance: str):
    # Lower Cap The Name
    return instance.lower().replace(" ", "_").replace("-", "")


# Page Model
# Start
class Page(TimestampAbstract):
    """
    Page is a webpage, that can be accessed by a route.
    Example: home page, can be accessed from this route /,
    """
    # Page Name
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Page"


# End


# Page Section
# Start
class PageSection(TimestampAbstract):
    """
    Each Page has a section, for example, About Section of a page, which is related to a page
    """
    # Section of a page
    page = models.ForeignKey(to=Page, on_delete=models.SET_NULL, null=True)
    # Page Section Name
    name = models.CharField(max_length=200)
    # Slug Field
    slug = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return f"{self.page.name} > {self.name}"

    def save(self, *args, **kwargs):
        if (not self.slug) and self.name:
            self.slug = create_underscore_slug(self.name)

        super(PageSection, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Page Section"
        verbose_name_plural = "Page Sections"


# End

# Page Component
# Start
class PageComponent(TimestampAbstract):
    """
    A Page component is a reusable component
    For example Contact Us Form
    """
    name = models.CharField(max_length=200)
    # Component Header
    header = models.CharField(max_length=200, blank=True)
    # Component Text
    text = models.CharField(max_length=200, blank=True)
    # Slug Field
    slug = models.CharField(blank=True, max_length=200)

    class Meta:
        verbose_name = "Page Component"
        verbose_name_plural = "Page Components"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if (not self.slug) and self.name:
            self.slug = create_underscore_slug(self.name)

        super(PageComponent, self).save(*args, **kwargs)


# End

# Text Content Abstract
# Start
class TextContentAbstract(TimestampAbstract):
    # Section Content Name
    name = models.CharField(max_length=200)
    # Section Sub Header
    sub_header = models.CharField(max_length=200, blank=True)
    # Header
    header = models.CharField(max_length=200, blank=True)
    # Text
    text = models.TextField(blank=True)
    # Icon
    icon = IconField(blank=True, null=True)
    # Slug Field
    slug = models.CharField(blank=True, max_length=200)
    # Image
    image = models.ImageField(blank=True, null=True)
    # Image Alt Text
    image_alt = models.TextField(max_length=200, blank=True, null=True)

    def image_view(self):
        return mark_safe('<img src="%s" width="400" height="auto" />' % self.image.url)

    image_view.short_description = 'Image'

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.image:
            self.image = File(compress_image(self.image), self.image.name)

        if (not self.slug) and self.name:
            self.slug = create_underscore_slug(self.name)

        super(TextContentAbstract, self).save(*args, **kwargs)


# End

# Section Text Content
# Start
class SectionTextContent(TextContentAbstract):
    # Page
    page = models.ForeignKey(to=Page, on_delete=models.SET_NULL, null=True, blank=True)
    # Section
    section = models.ForeignKey(to=PageSection, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.section.name} > {self.name}"

    def save(self, *args, **kwargs):
        if self.section:
            self.page = self.section.page

        if (not self.slug) and self.name:
            self.slug = create_underscore_slug(self.name)

        super(SectionTextContent, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Section Text Content"
        verbose_name_plural = "Section Text Contents"


# End

# Start Section Image Content
class SectionImageContent(TimestampAbstract):
    # Image Name
    name = models.CharField(max_length=200, blank=True)
    # Page Section
    section = models.ForeignKey(to=PageSection, on_delete=models.SET_NULL, null=True)
    # Image
    image = models.ImageField(blank=True, null=True)
    # Image Alt Text
    image_alt = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.section} > {self.name}"

    def image_view(self):
        return mark_safe('<img src="%s" width="400" height="auto" />' % self.image.url)

    image_view.short_description = 'Image'

    def save(self, *args, **kwargs):
        if self.image:
            self.image = File(compress_image(self.image), self.image.name)

        super(SectionImageContent, self).save(*args, **kwargs)


# Component Text Content
# Start
class ComponentTextContent(TextContentAbstract):
    component = models.ForeignKey(to=PageComponent, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.component.name} > {self.name}"

    def clean(self):
        if (not self.slug) and self.name:
            self.slug = create_underscore_slug(self.name)

    class Meta:
        verbose_name = "Component Text Content"
        verbose_name_plural = "Component Text Contents"


# End

# Meta Tags Global
class MetaTag(models.Model):
    # Name
    name = models.CharField(max_length=200)
    # Meta Tag
    tag = models.TextField()

    def __str__(self):
        return self.name
