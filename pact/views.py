from django.shortcuts import redirect, render
from django.http import HttpResponseForbidden
from django.contrib import messages

from circle.models import Project, Content
from pact.models import Pact, Buddy, Checkin
from pact.forms import PactForm, BuddyRequestForm, BuddyStatusForm




def pact_list(request):
    buddy_requests = Buddy.objects.filter(user=request.user).filter(status=1)
    my_pacts = request.user.pact_set.all().filter(status=1)
    buddy_pending = Buddy.objects.filter(status=1)
    buddy_queryset = Buddy.objects.filter(user=request.user).filter(status=2)
    buddy_pacts = Pact.objects.filter(id__in=buddy_queryset.values('pact_id')).filter(status=1)

    return render(request, 'pact/list.html', {
        'buddy_requests': buddy_requests,
        'my_pacts':my_pacts,
        'buddy_pacts':buddy_pacts,
        'buddy_queryset':buddy_queryset,
        })



def pact_read(request, pact_id):
    pact = Pact.objects.get(id=pact_id)
    checkins = pact.checkin_set.all()

    return render(request, 'pact/read.html', {
        'pact':pact,
        'checkins':checkins,
        })





def buddy_create(request, pact_id):
    pact = Pact.objects.get(id=pact_id)
    buddyform = BuddyRequestForm()
    
    if request.user != pact.owner:
        return HttpResponseForbidden()
    
    if request.method == 'POST':
        buddyform = BuddyRequestForm(request.POST)
        if buddyform.is_valid():
            buddy = buddyform.save(commit=False)
            buddy.pact = pact
            buddy.save()
            buddyform.save_m2m()
            
            return redirect('pact_list')
    
    return render(request, 'buddy/create.html', {
        'buddyform': buddyform,
        'pact': pact
        })

    

def buddy_status(request, buddy_id):
    buddy = Buddy.objects.get(id=buddy_id)
    buddyform = BuddyStatusForm(request.POST or None, instance=buddy)
    
    
    if buddyform.is_valid():
        buddy = buddyform.save()
        messages.success(request, 'Your response was processed.')
        return redirect('pact_list')
    
    return render(request, 'buddy/update.html', {
        'form': buddyform,
        'buddy': buddy
        })       





def pact_checkin(request, pact_id):
    pact = Pact.objects.get(id=pact_id)
    
    if pact.is_approved_buddy(request.user):
        checkin = Checkin(pact=pact, submitted_by=request.user)
        messages.success(request, 'Thank you for checking in.')
        checkin.save()
        return redirect('circle_menu') 

