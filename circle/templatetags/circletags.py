from django import template
from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.contrib import messages
from circle.models import Circle, Link, Project, Content
from circle.forms import CircleForm, CircleStartForm
from registry import views 
from registry.models import Registry


register = template.Library()


@register.inclusion_tag('content/slip.html')
def content_slip(content_id):
    content = Content.objects.get(id=content_id)

    return {
            'content':content,
           }
       

@register.inclusion_tag('circle/portal.html')
def portal_slip(circle_id, link_id):
    circle = Circle.objects.get(id=circle_id)
    link = Link.objects.get(id=link_id)
    child_circles = link.options.all()


    return {
            'circle':circle,
            'link':link,
            'child_circles':child_circles,
           }



@register.inclusion_tag('project/slip.html')
def project_slip(project_id):
    project = Project.objects.get(id=project_id)
    contents = project.content_set.all()

    return {
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



