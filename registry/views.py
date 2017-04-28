from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from allauth.account.decorators import verified_email_required
from circle.models import Circle, Link, Project, Content, Guideline
from registry.models import Registry, Contact
from registry.forms import RegistryForm, RegistryStartForm, ContactForm
from palette.models import Palette



@verified_email_required
def registry_list(request):
	my_registrys = Registry.objects.filter(creator=request.user)

	return render(request, 'registry/list.html', {
		'my_registrys':my_registrys,
		})

@verified_email_required
def registry_create(request):
	registrystartform = RegistryStartForm()

	if request.method == 'POST':
		registrystartform = RegistryStartForm(request.POST)
		if registrystartform.is_valid():
			registry = registrystartform.save(commit=False)
			registry.creator = request.user
			registry.save()
			messages.success(request, 'You created a new Registry')
                
			return redirect('registry_update', registry_id=registry.id)
    
	return render(request, 'registry/create.html', {'form': registrystartform})


@verified_email_required
def registry_update(request, registry_id):
	registry = Registry.objects.get(id=registry_id)
	registryform = RegistryForm(instance=registry)

	if request.method == 'POST':
		registryform = RegistryForm(request.POST, instance=registry)
		if registryform.is_valid():
			registry.save()
                
			return redirect('registry_update', registry_id=registry.id)
    
	return render(request, 'registry/update.html', {
		'registry':registry,
		'form': registryform,
		})



def registry_dashboard(request, registry_id):
	registry = Registry.objects.get(id=registry_id)
	contacts = registry.contact_set.all()
	circles = registry.circle_set.all()
	projects = registry.project_set.all()
	links = registry.link_set.all()

	return render(request, 'registry/dashboard.html', {
		'registry':registry,
		'circles':circles,
		'projects':projects,
		'contacts':contacts,
		'links':links,
		})







@verified_email_required
def contact_create(request, registry_id):
	registry = Registry.objects.get(id=registry_id)
	contactform = ContactForm()

	if request.method == 'POST':
		contactform = ContactForm(request.POST)
		if contactform.is_valid():
			contact = contactform.save(commit=False)
			contact.creator = request.user
			contact.registry = registry
			contact.save()
			messages.success(request, 'You created a new contact')
                
			return redirect('pregistry_dashboard', registry_id=registry.id)
    
	return render(request, 'contact/update.html', {'form': contactform})


@verified_email_required
def contact_update(request, contact_id):
	contact = Contact.objects.get(id=contact_id)
	contactform = ContactForm(instance=contact)

	if request.method == 'POST':
		contactform = ContactForm(request.POST)
		if contactform.is_valid():
			contact.save()
			messages.success(request, 'You updated this contact')
                
			return redirect(registry_list)
    
	return render(request, 'contact/update.html', {
		'contact':contact,
		'form': contactform,
		})

@verified_email_required
def contact_read(request, contact_id):
	contact = Contact.objects.get(id=contact_id)

	return render(request, 'contact/read.html', {
		'contact':contact,
		})