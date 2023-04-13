from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort = request.GET.get('sort')
    if sort == 'name':
        phones = Phone.objects.order_by('name')
    elif sort == 'price_asc':
        phones = Phone.objects.order_by('price')
    elif sort == 'price_desc':
        phones = Phone.objects.order_by('-price')
    else:
        phones = Phone.objects.all()
    return render(request, 'catalog.html', {'phoness': phones})


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'product.html', {'phones': phone})