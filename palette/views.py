from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from allauth.account.decorators import verified_email_required
from registry.models import Registry
from palette.forms import PaletteStartForm, PaletteForm
from palette.models import Palette


@verified_email_required
def palette_create(request, registry_id):
	registry = Registry.objects.get(id=registry_id)
	palettestartform = PaletteStartForm()

	if request.method == 'POST':
		palettestartform = PaletteStartForm(request.POST)
		if palettestartform.is_valid():
			palette = palettestartform.save(commit=False)
			palette.creator = request.user
			registry.palette = palette
			palette.save()
			messages.success(request, 'You created a new palette')
                
			return redirect('palette_update', palette_id=palette.id)
    
	return render(request, 'palette/update.html', {'form': palettestartform})


@verified_email_required
def palette_update(request, palette_id):
	palette = Palette.objects.get(id=palette_id)
	paletteform = PaletteForm(instance=palette)

	if request.method == 'POST':
		paletteform = PaletteForm(request.POST)
		if paletteform.is_valid():
			palette.save()
			messages.success(request, 'You updated this palette')
                
			return redirect('palette_update', palette_id=palette.id)
    
	return render(request, 'palette/update.html', {
		'palette':palette,
		'form': paletteform,
		})

@verified_email_required
def palette_read(request, palette_id):
	palette = Palette.objects.get(id=palette_id)

	return render(request, 'palette/read.html', {
		'palette':palette,
		})