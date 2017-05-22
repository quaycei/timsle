from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from django.contrib import messages

from circle.models import Project, Content
from pact.models import Pact, Buddy, Checkin


def menu(request):
    return redirect('circle_menu') 

def start(request):
    return redirect('timsle_lander') 