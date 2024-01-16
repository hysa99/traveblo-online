from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from django.db.models import Q
from .forms import NewItemForm, EditItemForm
from .models import Item






# Create your views here.
def browse(request):
    query = request.GET.get('query', '')
    items = Item.objects.filter(is_active=True)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(price__icontains=query))
    
    return render(request, 'browse.html', {
        'items': items,
        'query': query,
    })


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    releated_items = Item.objects.filter().exclude(pk=pk)[0:15]

    return render(request, 'detail.html', {
        'item': item,
        'releated_items': releated_items
    })


@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.published_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'forms.html', {
        'form': form,
        'title': 'New Item'
    })



@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, published_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            item = form.save(commit=False)
            item.published_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'forms.html', {
        'form': form,
        'title': 'Edit Item'
    })



@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, published_by=request.user)
    item.delete()

    return redirect('dashboard:dashboard')