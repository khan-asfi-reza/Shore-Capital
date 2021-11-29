import nested_admin.nested
from django.contrib import admin

from Contact.models.contact import ContactUsMessage
from Pages.models.page import Page, PageSection, SectionTextContent, PageComponent, ComponentTextContent, \
    SectionImageContent, MetaTag


# Contact Us Admin Panel
# Start
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "replied", "created_on"]


admin.site.register(ContactUsMessage, ContactUsAdmin)


# End

# Start
# Text Content Inline
class TextContentInline(nested_admin.nested.NestedStackedInline):
    model = SectionTextContent
    fields = ["name", "sub_header", "header", "text", "icon", "image", "image_view"]
    extra = False
    readonly_fields = ["image_view"]


# Start
# Image Content Inline
class ImageContentInline(nested_admin.nested.NestedStackedInline):
    extra = False
    model = SectionImageContent
    fields = ["name", "image", "image_alt", "image_view"]
    readonly_fields = ["image_view"]


# Page Section Inline
class PageSectionList(nested_admin.nested.NestedStackedInline):
    model = PageSection
    extra = False
    fields = ["name", "page"]
    inlines = [TextContentInline, ImageContentInline]


# Page Admin
class PageAdmin(nested_admin.nested.NestedModelAdmin):
    list_display = ["name", "created_on", "updated_on"]
    inlines = [PageSectionList]


admin.site.register(Page, PageAdmin)


# End

# Page Section
# Start
class PageSectionAdmin(admin.ModelAdmin):
    list_display = ["name", "page", "created_on"]
    list_filter = ["page"]
    inlines = [TextContentInline]


admin.site.register(PageSection, PageSectionAdmin)


# End

# Page Component Content Inline
# Text Content Inline
# Start
class ComponentTextContentInline(nested_admin.nested.NestedStackedInline):
    model = ComponentTextContent
    fields = ["name", "sub_header", "header", "text", "icon"]
    extra = False


# End

# Text Content Inline
# Start
class PageComponentAdmin(nested_admin.nested.ModelAdmin):
    model = PageComponent
    list_display = ["name", "header", "created_on", "id"]
    extra = False
    inlines = [ComponentTextContentInline]


admin.site.register(PageComponent, PageComponentAdmin)


# End

class MetaTagAdmin(admin.ModelAdmin):
    list_display = ["name", "id"]


admin.site.register(MetaTag, MetaTagAdmin)
