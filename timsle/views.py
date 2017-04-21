from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from allauth.account.decorators import verified_email_required
from circle.models import Circle, Link, Project, Content, Guideline
from registry.models import Registry, Contact
from pact.models import Pact, Buddy, Checkin
from registry import views
from timsle.models import Line


def timsle_lander(request):
    circles = Circle.objects.all()
    lines = Line.objects.all()

    return render(request, 'timsle/lander.html', {
        'circles': circles,
        'lines':lines,
        })
