from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, DetailView
from django.template import loader
from .models import Prodotto

def index(request):

    template = loader.get_template('home-02.html')
    return HttpResponse(template.render(None, request))

class ProductView(TemplateView):
    template_name = "product.html"

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        products = Prodotto.objects.all()
        context['products'] = products
        return context


class ProductDetail(DetailView):

    model = Prodotto
    template_name = "product-detail.html"

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        return context


def cart(request):
    template = loader.get_template('cart.html')
    return HttpResponse(template.render(None, request))


def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render(None, request))


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render(None, request))


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render(None, request))
