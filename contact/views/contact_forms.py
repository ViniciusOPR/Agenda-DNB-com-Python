from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from contact.models import Contact


def create(request):
    if request.method == 'POST':
        print()
        print(request.method)
        print(request.POST.get('AKA'))
        print(request.POST.get('name'))
        print()
    
    context = {}
    print()
    print(request.method)
    print()
    return render(request, 'contact/create.html', context)