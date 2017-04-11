from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from allauth.account.decorators import verified_email_required

from circle.models import Circle, Project, Content, Guideline
from pact.models import Pact, Buddy, Checkin


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
	child_circles = circle.circle_set.all().filter(parent=circle).filter(verification=1).filter(status=1)
	projects = circle.project_set.all().filter(status=1)

	return render(request, 'circle/list.html',{
		'circle':circle,
		'child_circles':child_circles,
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
