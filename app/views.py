from datetime import date
from dateutil.parser import parse

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from raven.contrib.django.raven_compat.models import client
from app.models import Item
from app.forms import ProfileForm
from app.utils import parse_inbound


def index(request):
    if request.user.is_authenticated():
        return redirect('/dashboard/')

    return render(request, 'index.html')


@login_required
def dashboard(request, the_date=None):
    the_date = parse(the_date).date() if the_date else date.today()
    
    users = User.objects.exclude(pk=-1)

    return render(request, 'dashboard.html', {'users': users, 'the_date': the_date})

@login_required
def settings(request):
    form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    if form.is_valid():
        profile = form.save(commit=False)
        profile.user = request.user
        profile.save()

        return redirect('/dashboard/')

    return render(request, 'settings.html', {'form': form})


@csrf_exempt
@require_POST
def inbound(request):
    email, items = parse_inbound(request.body)

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        client.captureException()
        return HttpResponse('OK')

    for item in items:
        Item.objects.create(user=user, text=item).save()

    return HttpResponse('OK')
