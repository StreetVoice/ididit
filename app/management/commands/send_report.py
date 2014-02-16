from datetime import date, timedelta

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = User.objects.exclude(pk=-1)

        the_date = date.today() - timedelta(days=1)

        title = "IDIDIT Report %s" % the_date
        content = render_to_string('email/report.html', {'users': users, 'the_date': the_date})
        message = EmailMessage(title, content, settings.DEFAULT_FROM_EMAIL, [user.email for user in users],
            headers = {'Reply-To': settings.POSTMARK_INBOUND_EMAIL})
        message.content_subtype = 'html'
        message.send()
