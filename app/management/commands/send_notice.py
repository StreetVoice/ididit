from datetime import datetime, date, time, timedelta

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.core.mail import EmailMessage


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        now = datetime.now().time()

        start_time = time(now.hour, now.minute)
        end_time = (datetime.combine(date.today(), time(now.hour, now.minute)) + timedelta(minutes=10)).time()

        print "It's", start_time, '~', end_time

        users = User.objects.exclude(pk=-1)
        users = users.filter(profile__notice_at__range=(start_time, end_time))

        for user in users:
            print 'Sending notice to', user.username

            title = "What you have done today?"
            content = render_to_string('email/notice.html')
            message = EmailMessage(title, content, settings.DEFAULT_FROM_EMAIL, [user.email],
                headers = {'Reply-To': settings.POSTMARK_INBOUND_EMAIL})
            message.content_subtype = 'html'
            message.send()
