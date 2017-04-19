from django.shortcuts import redirect, render, get_object_or_404, reverse
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from allauth.account.decorators import verified_email_required
from circle.models import Circle, Link, Project, Content, Guideline
from registry.models import Registry, Contact
from pact.models import Pact, Buddy, Checkin
from circle.forms import CircleForm, ProjectForm
from registry import views


@verified_email_required
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
	guideline_examples = content.guideline_set.all().filter(type_of_guideline=0)
	guideline_rules = content.guideline_set.all().filter(type_of_guideline=1)


	return render(request, 'content/read.html',{
		'project':project,
		'content':content,
		'guideline_examples':guideline_examples,
		'guideline_rules':guideline_rules,
		})


@verified_email_required
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


@verified_email_required
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

@verified_email_required
def circle_create(request, registry_id):
	registry = Registry.objects.get(id=registry_id)
	circleform = CircleForm()

	if request.method == 'POST':
		circleform = CircleForm(request.POST)
		if circleform.is_valid():
			circle = circleform.save(commit=False)
			circle.creator = request.user
			circle.registry = registry
			circle.palette = registry.palette
			circle.verification = registry.verification
			circle.save()
			messages.success(request, 'You created a new circle')
			return redirect('circle_list', circle_id=circle.id)
                
	else:
		circleform = CircleForm()

    
	return render(request, 'circle/update.html', {'form': circleform})





@verified_email_required
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