from django.shortcuts import render

from .models import IceCream


def index(request):
    template = 'ice_cream/index.html'
    # только то мороженое, у кторого есть флаг on_main
    selected_ice_creams = IceCream.objects.filter(on_main=True)
    context = {
        'selected_ice_creams': selected_ice_creams,
    }
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/ice_cream_list.html'
    # все мороженое
    ice_creams = IceCream.objects.all()
    context = {
        'ice_creams': ice_creams,
    }
    return render(request, template, context)


def ice_cream_detail(request, pk):
    template = 'ice_cream/ice_cream_detail.html'
    ice_cream = IceCream.objects.get(pk=pk)
    context = {
        'ice_cream': ice_cream,
    }
    return render(request, template, context)