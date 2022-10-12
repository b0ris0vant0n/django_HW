from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'name':
        phone_objects = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phone_objects = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phone_objects = Phone.objects.all().order_by('-price')
    else:
        phone_objects = Phone.objects.all()

    context = {'phones' : phone_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_object = Phone.objects.filter(slug=slug)
    for phone in phone_object:
        context = {'phone': {'name': phone.name, 'price': phone.price, 'release_date': phone.release_date, 'lte_exists': phone.lte_exists, 'image': phone.image} }
    return render(request, template, context)
