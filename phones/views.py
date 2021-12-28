from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort', 'name')
    context = {
        'phones': Phone.objects.all().order_by(sort),
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones_objects = Phone.objects.all()
    for phone_obj in phones_objects:
        if phone_obj.slug == slug:
            phone = phone_obj
            context = {
                'phone': phone
            }
            return render(request, template, context)
