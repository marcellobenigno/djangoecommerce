from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

    def send_mail(self):
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message']
        }

        body = render_to_string('email.txt', context=context)

        send_mail(
            'Contato do Django E-Commerce', body, self.cleaned_data['email'],
            [self.cleaned_data['email'], settings.DEFAULT_FROM_EMAIL]
        )
