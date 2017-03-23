from django import template
from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse

from circle.models import Style, Group, Organization, Circle, Project, Content


register = template.Library()


@register.inclusion_tag('content/slip.html')
def content_slip(content_id):
    content = Content.objects.get(id=content_id)

    return {
            'content':content,
           }
       

@register.inclusion_tag('project/slip.html')
def project_slip(circle_slug, project_id):
    circle = Circle.objects.get(slug=circle_slug)
    project = Project.objects.get(id=project_id)
    contents = project.content_set.all()

    return {
        'circle':circle,
        'project':project,
        'contents':contents,
        }


@register.inclusion_tag('group/panel.html')
def group_panel(group_slug):
    group = Group.objects.get(slug=group_slug)
    circles = group.circle_set.all()
    projects = group.project_set.all()

    return {
        'group':group,
        'circles':circles,
        'projects':projects,
        }





