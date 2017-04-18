from django import template
from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.core.urlresolvers import reverse
from registry import views

from registry.models import Registry
from palette.models import Palette, Element
from palette.forms import PaletteForm


register = template.Library()




@register.inclusion_tag('palette/update.html', takes_context=True)
def palette_create(context, registry_id):
    request = context['request']
    registry = Registry.objects.get(id=registry_id)
    paletteform = PaletteForm()

    if request.method == 'POST':
        paletteform = PaletteForm(request.POST)
        if paletteform.is_valid():
            palette = paletteform.save(commit=False)
            palette.creator = registry.creator
            palette.registry = registry
            palette.save()
            return HttpResponseRedirect(registry_dashboar)
    else:
        paletteform = PaletteForm()

    return {
        'form':paletteform,
        'registry':registry,
        }





@register.inclusion_tag('palette/update.html', takes_context=True)
def palette_update(context, registry_id, palette_id):
    request = context['request']
    registry = Registry.objects.get(id=registry_id)
    palette = Palette.objects.get(id=palette_id)
    paletteform = PaletteForm(instance=palette_id)

    if request.method == 'POST':
        paletteform = PaletteForm(request.POST, instance=palette)
        if paletteform.is_valid():
            palette.save()
                
            return {
                'form':paletteform,
                'palette':palette,
                'registry':registry,
                }


    return {
        'form':paletteform,
        'registry':registry,
        }





