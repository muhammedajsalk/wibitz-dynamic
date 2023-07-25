from django.forms import ModelForm
from web.models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
