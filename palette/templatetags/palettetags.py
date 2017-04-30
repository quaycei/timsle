from django import template
from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.contrib import messages
from palette.models import Palette
from palette.forms import PaletteStartForm
from registry import views 
from registry.models import Registry


register = template.Library()


@register.inclusion_tag('palette/update.html', takes_context=True)
def palette_create(context, registry_id):
    request = context['request']
    registry = Registry.objects.get(id=registry_id)
    palettestartform = PaletteStartForm()

    if request.method == 'POST':
        palettestartform = PaletteStartForm(request.POST)
        if palettestartform.is_valid():
            palette = palettestartform.save(commit=False)
            palette.name = registry.name
            registry.palette = palette
            palette.save()
            messages.success(request, 'You created a new palette')
                
            return redirect('registry_update', registry_id=registry.id)
    
    return  {'form': palettestartform}



