import random
import string

from fontawesome_5 import Icon

from Pages.const import PAGES, CLASS_PAGE_COMPONENTS
from Pages.models.page import Page, PageSection, SectionTextContent, \
    PageComponent, create_underscore_slug, ComponentTextContent, SectionImageContent
from ShoreCapital.settings import STATICFILES_DIRS
from django.core.files.uploadedfile import UploadedFile


def img_dir(img):
    return STATICFILES_DIRS[0] / "img/" / img


def get_random_name():
    r_string = string.ascii_lowercase + string.digits
    return "".join([random.choice(r_string) for i in range(20)])


def create_content(ModelInstance, contents, **kwargs):
    for content in contents:
        image = content.pop("image", None)
        icon = content.pop("icon", "")
        if icon:
            icon = Icon(**icon)

        created_content = ModelInstance.objects.create(
            **content,
            **kwargs,
            icon=icon
        )
        if image:
            ext = image.split(".")[-1]

            file = str(img_dir(image))
            created_content.image.save(get_random_name() + '.' + ext,
                                       UploadedFile(open(file, 'rb'), content_type=f"image/{ext}"))

        created_content.save()


def create_image(ModelInstance, images: dict, **kwargs):
    for image in images:
        image_created = ModelInstance.objects.create(
            name=image["name"],
            image_alt=image.get("image_alt", ""),
            **kwargs
        )
        ext = image["image"].split(".")[-1]
        file = str(img_dir(image["image"]))
        image_created.image.save(
            get_random_name() + '.' + ext,
            UploadedFile(open(file, 'rb'), content_type=f"image/{ext}")
        )
        image_created.save()


def create_default_pages():
    # Create page and contents
    for page in PAGES:
        # Create Page
        page_object = Page.objects.create(name=page["name"])
        # Create Section and Contents
        for key, section in enumerate(page["sections"]):
            # Get Section Name
            section_name = section.get("name", f"SECTION_#{key}")
            # Get Section Slug
            slug = section.get("slug", create_underscore_slug(section_name))
            # Create Section
            section_object = PageSection.objects.create(
                name=section_name,
                slug=slug,
                page=page_object
            )
            # Create Section Contents
            create_content(SectionTextContent, section["contents"], section=section_object)

            images = section.get("images", None)

            if images:
                create_image(SectionImageContent, images, section=section_object)

    # Create Page Component
    for component in CLASS_PAGE_COMPONENTS:
        # Create Component
        contents = component.pop("contents", None)
        comp = PageComponent.objects.create(**component)
        # Check if contents
        if contents:
            create_content(ComponentTextContent, contents, component=comp, )
