from django.forms import ModelForm
from django import forms

from Contact.models.contact import ContactUsMessage


class ContactForm(ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput())
    email = forms.CharField(required=True, widget=forms.TextInput())
    message = forms.CharField(required=True,
                              widget=forms.Textarea(attrs={"contenteditable": 'false',
                                                           "id": "textarea_ce",
                                                           "cols": 0,
                                                           "rows": 0}))

    class Meta:
        model = ContactUsMessage
        fields = ["name", "email", "message"]

    def clean(self):
        super(ContactForm, self).clean()
