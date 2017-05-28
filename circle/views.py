from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from circle.models import Circle, Link, Project, Content, Guideline
from registry.models import Registry, Contact
from pact.models import Pact, Buddy, Checkin
from circle.forms import CircleForm, CircleStartForm, ProjectForm, LinkForm
from registry import views



def circle_menu(request):
    buddy_requests = Buddy.objects.filter(user=request.user).filter(status=1)
    my_pacts = request.user.pact_set.all().filter(status=1)
    buddy_pending = Buddy.objects.filter(status=1)
    buddy_queryset = Buddy.objects.filter(user=request.user).filter(status=2)
    buddy_pacts = Pact.objects.filter(id__in=buddy_queryset.values('pact_id')).filter(status=1)

    return render(request, 'circle/menu.html', {
        'buddy_requests': buddy_requests,
        'my_pacts':my_pacts,
        'buddy_pacts':buddy_pacts,
        'buddy_queryset':buddy_queryset,
        })


def circle_list(request, circle_id):
	circle = Circle.objects.get(id=circle_id)
	links = circle.link_set.all().filter(connection_type=0)
	projects = circle.project_set.all().filter(status=1)

	return render(request, 'circle/list.html',{
		'circle':circle,
		'links':links,
		'projects':projects,
		})


def group_list(request):
	torus_circles = Circle.objects.all().filter(rank=0).filter(verification=1).filter(status=1)
	projects = Project.objects.filter(status=1)

	return render(request, 'group/list.html',{
		'torus_circles':torus_circles,
		'projects':projects,
		})


def project_read(request, project_id):
	project = Project.objects.get(id=project_id)
	contents = project.content_set.all()

	return render(request, 'project/read.html',{
		'project':project,
		'contents':contents,
		})


def content_read(request, project_id, content_id):
	project = Project.objects.get(id=project_id)
	content = Content.objects.get(id=content_id)


	return render(request, 'content/read.html',{
		'project':project,
		'content':content,
		})



def project_create(request, registry_id):
	registry = Registry.objects.get(id=registry_id)
	projectform = ProjectForm()

	if request.method == 'POST':
		projectform = ProjectForm(request.POST)
		if projectform.is_valid():
			project = projectform.save(commit=False)
			project.creator = request.user
			project.registry = registry
			project.verification = registry.verification
			project.palette = registry.palette
			project.verification = registry.verification
			project.save()
			messages.success(request, 'You created a new project')
                
			return redirect('project_read', project_id=project.id)
    
	return render(request, 'project/update.html', {'form': projectform})



def project_update(request, project_id):
	project = Project.objects.get(id=project_id)
	projectform = ProjectForm(instance=project)

	if request.method == 'POST':
		projectform = ProjectForm(request.POST)
		if projectform.is_valid():
			project.save()
			messages.success(request, 'You updated this project')
                
			return redirect('project_read', project_id=project.id)
    
	return render(request, 'project/update.html', {
		'project':project,
		'form': projectform,
		})


def circle_create(request, registry_id, circle_group):
	registry = Registry.objects.get(id=registry_id)
	users = registry.circle_set.all().filter(group=0).order_by('-created_at')
	circlestartform = CircleStartForm()
	example_users = Guideline.objects.filter(purpose=3).filter(type_of_guideline=0)

	if request.method == 'POST':
		circlestartform = CircleStartForm(request.POST)
		if circlestartform.is_valid():
			circle = circlestartform.save(commit=False)
			circle.group = circle_group
			circle.creator = request.user
			circle.registry = registry
			circle.palette = registry.palette
			circle.verification = registry.verification
			circle.save()
			messages.success(request, 'You created a new circle')
			return redirect('circle_create', 
				registry_id=registry.id, circle_group=circle.group
				)
                
	else:
		circlestartform = CircleStartForm()

    
	return render(request, 'circle/create_user.html', {
		'registry':registry,
		'form': circlestartform,
		'users': users,
		'example_users':example_users,
		'circle_group': circle_group,
	})





def circle_create_filter(request, registry_id):
	registry = Registry.objects.get(id=registry_id)
	filters = registry.circle_set.all().filter(group=3).order_by('-created_at')
	example_offerings = Guideline.objects.filter(purpose=4).filter(type_of_guideline=0)
	circlestartform = CircleStartForm()

	if request.method == 'POST':
		circlestartform = CircleStartForm(request.POST)
		if circlestartform.is_valid():
			circle = circlestartform.save(commit=False)
			circle.group = 3
			circle.creator = request.user
			circle.registry = registry
			circle.palette = registry.palette
			circle.verification = registry.verification
			circle.save()
			messages.success(request, 'You created a new circle')
			return redirect('circle_create_offering', 
				registry_id=registry.id,
				)
                
	else:
		circlestartform = CircleStartForm()

    
	return render(request, 'circle/create_offering.html', {
		'registry':registry,
		'form': circlestartform,
		'filters':filters,
		'example_offerings':example_offerings,
	})





def circle_create_types(request, registry_id, circle_id):
	registry = Registry.objects.get(id=registry_id)
	circles = registry.circle_set.all()
	circlestartform = CircleStartForm()
	parent_circle = Circle.objects.get(id=circle_id)

	if request.method == 'POST':
		circlestartform = CircleStartForm(request.POST)
		if circlestartform.is_valid():
			circle = circlestartform.save(commit=False)
			circle.creator = request.user
			circle.registry = registry
			circle.palette = registry.palette
			circle.verification = registry.verification
			circle.save()
			link = Link(registry=registry, creator=request.user, verification=registry.verification)
			link.save()
			link.circle = parent_circle
			link.options.add(circle)
			link.save()
			messages.success(request, 'You created a new circle')
			return redirect('circle_create_types', 
				registry_id=registry.id,
			 	circle_id=circle.id,
			 	)
                
	else:
		circlestartform = CircleStartForm()

    
	return render(request, 'circle/update.html', {
		'parent_circle':parent_circle,
		'registry':registry,
		'form': circlestartform,
		'circles':circles,
	})





def circle_update(request, circle_id):
	circle = Circle.objects.get(id=circle_id)
	circleform = CircleForm(instance=circle)

	if request.method == 'POST':
		circleform = CircleForm(request.POST, instance=circle)
		if circleform.is_valid():
			circle.save()
			messages.success(request, 'You updated this circle')
                
			return redirect('circle_list', circle_id=circle.id)
    
	return render(request, 'circle/update.html', {
		'circle':circle,
		'form': circleform,
		})




def link_create(request, registry_id):
	registry = Registry.objects.get(id=registry_id)
	linkform = LinkForm()

	if request.method == 'POST':
		linkform = LinkForm(request.POST)
		if linkform.is_valid():
			link = linkform.save(commit=False)
			link.creator = request.user
			link.registry = registry
			link.verification = registry.verification
			link.save()
			linkform.save_m2m()
			messages.success(request, 'You created a new link')
			return redirect('circle_list', circle_id=link.circle.id)
                
	else:
		linkform = LinkForm()

    
	return render(request, 'link/update.html', {
		'registry':registry,
		'form': linkform,
		})






def link_update(request, link_id):
	link = Link.objects.get(id=link_id)
	linkform = LinkForm(instance=link)

	if request.method == 'POST':
		linkform = LinkForm(request.POST, instance=link)
		if linkform.is_valid():
			link.save()
			linkform.save()
			messages.success(request, 'You updated this link')
                
			return redirect('circle_list', circle_id=link.circle.id)
    
	return render(request, 'link/update.html', {
		'link':link,
		'form': linkform,
		})

