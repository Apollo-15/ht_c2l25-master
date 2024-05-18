from django.shortcuts import render, get_object_or_404
from .models import IceCream, Review
from .forms import ReviewForm

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

def ice_cream_reviews(request, pk):
    ice_cream = get_object_or_404(IceCream, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.ice_cream = ice_cream
            review.save()
    else:
        form = ReviewForm()
    return render(request, 'ice_cream/ice_cream_reviews.html', {'form': form, 'ice_cream': ice_cream})
