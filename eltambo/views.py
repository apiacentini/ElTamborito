from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, DetailView
from django.template import loader
from django.views.generic.edit import FormView
from .models import Prodotto
from .models import Utente
from .models import Indirizzo
from django.urls import reverse_lazy
from django.db.models import Q
from .forms import UserRegistrationForm


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


class ProductOnSale(TemplateView):
    template_name = "product.html"

    def get_context_data(self, **kwargs):
        context = super(ProductOnSale, self).get_context_data(**kwargs)
        products = Prodotto.objects.all().filter( Q(caratteristiche__contains='3') | Q(caratteristiche__contains='4'))
        context['products'] = products
        return context


def cart(request):
    template = loader.get_template('cart.html')
    return HttpResponse(template.render(None, request))


def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render(None, request))


def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render(None, request))


class SignupView(FormView):
    template_name = 'newLogin.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = Utente.objects.create(email=cleaned_data['email'],
                                            nome=cleaned_data['first_name'],
                                            cognome=cleaned_data['last_name'],
                                            password=cleaned_data['password'])
            indirizzo = Indirizzo.objects.create(nazione=cleaned_data['nazione'],
                                            citta=cleaned_data['citta'],
                                            via=cleaned_data['via'],
                                            provincia=cleaned_data['provincia'],
                                            CAP=cleaned_data['cap'])
            try:
                user.save()
                user.indirizzo.add(indirizzo)
            except Exception as saving_ex:
                print(saving_ex)
            finally:
                return super(SignupView, self).form_valid(form)
