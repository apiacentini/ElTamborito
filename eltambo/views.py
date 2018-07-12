from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Prodotto

def index(request):
    template = loader.get_template('home-02.html')
    return HttpResponse(template.render(None, request))

def product(request):
    template = loader.get_template('product.html')
    return HttpResponse(template.render(None, request))

def detail(request, product_id):
    product = get_object_or_404(Prodotto, pk=product_id)
    return render(request, 'product-detail.html', {'product':product})

def cart(request):
    template = loader.get_template('cart.html')
    return HttpResponse(template.render(None, request))
