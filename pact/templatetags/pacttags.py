from django import template
from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse

from pact.models import Pact


register = template.Library()


@register.inclusion_tag('pact/my_panel.html')
def my_pact_panel(pact_id):
    pact = Pact.objects.get(id=pact_id)
    checkins = pact.checkin_set.all()[:10]

    return {
            'pact':pact,
            'checkins':checkins,
           }


@register.inclusion_tag('pact/buddy_panel.html')
def buddy_pact_panel(pact_id):
    pact = Pact.objects.get(id=pact_id)
    checkins = pact.checkin_set.all()[:10]

    return {
            'pact':pact,
            'checkins':checkins,
           }
       





