from django.views.generic import TemplateView

from Contact.form import ContactForm
from Pages.models.page import SectionTextContent, PageSection, MetaTag, PageComponent, ComponentTextContent, SectionImageContent


class PageTemplateView(TemplateView):
    page_name = ""
    contact_form = ContactForm
    component_queryset = None

    @staticmethod
    def get_component_header(component):
        return {
            "header": component.header,
            "text": component.text
        }

    def get_components(self):
        components = ["contact_us", "testimonial"]
        component_context = {}
        if self.component_queryset:
            pass

        for component in components:
            comp = PageComponent.objects.filter(slug=component)
            if comp.exists():
                component_context.update(
                    {f"{component}": {
                        **self.get_component_header(comp.first()),
                        "contents": ComponentTextContent.objects.filter(component=comp.first())
                    }}
                )
        return component_context

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        # Get Sections
        page_content = {}
        image_content = {}
        sections = PageSection.objects.filter(page__name=self.page_name)
        # For Each Section Get Content
        for section in sections:
            # Text Content
            content_queryset = SectionTextContent.objects.filter(section=section)
            page_content.update(
                {
                    f"{section.slug}": content_queryset
                }
            )
            # Image Content
            image_queryset = SectionImageContent.objects.filter(section=section)
            image_content.update(
                {
                    f"{section.slug}": image_queryset
                }
            )
        # Send Via Context
        context["contents"] = page_content
        context["images"] = image_content
        # Page Name for Active Page
        context["page_name"] = self.page_name
        # Meta Tags
        context["meta_tags"] = MetaTag.objects.all()
        # Form Submission State
        context["form"] = self.contact_form()
        context["formSubmitted"] = False
        # Component List
        context["components"] = self.get_components()
        return context

    def post(self, request, *args, **kwargs):
        # Get Form
        form = self.contact_form(request.POST)
        # Set Context
        context = self.get_context_data(**kwargs)
        # Check if form is valid
        if form.is_valid():
            form.save()
            context["formSubmitted"] = True
        else:
            context["formError"] = True

        return self.render_to_response(context)


class HomeView(PageTemplateView):
    template_name = "index.html"
    page_name = "Home"


class BuyView(PageTemplateView):
    template_name = "buy.html"
    page_name = "Buy"


class SellView(PageTemplateView):
    template_name = "sell.html"
    page_name = "Sell"


class CareerView(PageTemplateView):
    template_name = "careers.html"
    page_name = "Careers"


class ReferralView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(ReferralView, self).get_context_data()
        context["meta_tags"] = MetaTag.objects.all()
        return context

    template_name = "referral.html"
