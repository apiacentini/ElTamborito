from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime
from django.views.generic import TemplateView, DetailView
from django.template import loader
from django.http import Http404
from django.views.generic.edit import FormView
from .models import Prodotto
from .models import Acquista
from .models import Utente
from .models import Indirizzo
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.db.models import Q, Sum
from django.db import IntegrityError

from .forms import *


def index(request):

    template = loader.get_template('home-02.html')
    return HttpResponse(template.render(None, request))


class ProductView(TemplateView):
    template_name = "product.html"


    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)

        if 'search' in self.request.GET:
            search_term = self.request.GET['search']
            products = Prodotto.objects.all().filter(modello__contains=search_term)
            context['products'] = products
            return context
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
        if 'search' in self.request.GET:
            search_term = self.request.GET['search']
            products = Prodotto.objects.all().filter( Q(caratteristiche__contains='3') | Q(caratteristiche__contains='4')).filter(modello__contains=search_term)
            context['products'] = products
            return context
        products = Prodotto.objects.all().filter( Q(caratteristiche__contains='3') | Q(caratteristiche__contains='4'))
        context['products'] = products
        return context


class cart(TemplateView):
    template_name = "cart.html"

    def get_context_data(self, **kwargs):
        context = super(cart, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = get_object_or_404(Utente, id=self.request.user.id)
            total1 = Acquista.objects.filter(utente=user).aggregate(Sum('prezzo'))
            totale2 = total1['prezzo__sum']
            context['total'] = totale2
            return context


def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render(None, request))


def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render(None, request))


class SignupView(FormView):
    template_name = 'newLogin.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = Utente.objects.create_user(username=cleaned_data['username'],
                                                first_name=cleaned_data['nome'],
                                                last_name=cleaned_data['cognome'],
                                                email=cleaned_data['email'],
                                                password=cleaned_data['password'])
            try:
                user.save()
            except Exception as saving_ex:
                print(saving_ex)
            except IntegrityError as e:
                print(e)
            finally:
                return super(SignupView, self).form_valid(form)



def add_product(req):
    if req.method == 'POST':
        userId = req.POST['userid']
        productId = req.POST['prodottoid']
        price = req.POST['price']
        user = get_object_or_404(Utente, id=userId)
        product = get_object_or_404(Prodotto, id=productId)

        product = Acquista.objects.create(
            utente = user,
            prodotto = product,
            quantita = 1,
            prezzo = price,
            data = timezone.now()
        )

        try:
            product.save()
            return HttpResponse("Bazinga!", content_type="text/plain")
        except Exception as saving_ex:
            raise Http404

