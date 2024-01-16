from django.shortcuts import render, get_object_or_404
from item.models import Item
from django.contrib.auth.decorators import login_required
from dashboard.models import Action

from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse


from item.models import Item




# Create your views here.
@login_required
def dashboard(request):
    items = Item.objects.filter(published_by=request.user)[0:10]

    return render(request, 'dashboards.html', {
        'items': items,
    })



def insights(request):
    items = Item.objects.filter(published_by=request.user)[0:10]
    actions = Action.objects.all()
    return render(request, 'insights.html', {
        'items': items,
        'actions': actions,
    })




def inbox(request):

    return render(request, 'inbox.html')

