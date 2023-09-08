from django.shortcuts import render, redirect
from .models import MessageRequestModel

# Create your views here.


def ListLeadsView(request):
    messageRequests = MessageRequestModel.objects.all().order_by('-status','-date_created')

    if request.method == 'POST' and 'complet_lead' in request.POST:
        leadID = request.POST.get('leadID')
        updateLead = MessageRequestModel.objects.get(id=leadID)
        updateLead.status = 'Complete'
        updateLead.openStatus = 'Viewed'
        updateLead.save()
        return redirect('list-leads')

    context = {
        "messageRequests": messageRequests
    }
    return render(request, 'leads/listLeads.html', context)
