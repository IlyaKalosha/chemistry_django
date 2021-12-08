import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView
from .forms import (
    PillSearchName, PillSearchCategory, PillSearchCost, PillSearchDate, AddPill, UpdatePill, DeletePill,
    RecipeSearchDate, RecipeSearchDoctor, DeleteRecipe, AddRecipe, UpdateRecipe)
from . import models
from .utils import django_admin_keyword_search


class Home(TemplateView):
    template_name = 'home.html'


class Pills(LoginRequiredMixin, View):
    template_name = 'pages/pills.html'

    def get_context_data(self, request, **kwargs):
        if 'pills_list' not in kwargs:
            if hasattr(request.user, 'manager'):
                kwargs['pills_list'] = models.Storage.objects.filter(pharmacy_id=request.user.manager.pharmacy_id)[:15]
            elif hasattr(request.user, 'seller'):
                kwargs['pills_list'] = models.Storage.objects.filter(
                    pharmacy_id=request.user.seller.manager_id.pharmacy_id)[:15]
            else:
                kwargs['pills_list'] = models.Storage.objects.all()[:15]
        return kwargs

    def get(self, request, *args, **kwargs):
        context = {}
        if 'storageId' in request.GET:
            current_order = models.Order.objects.filter(is_agreed=False)
            current_pill = request.GET.get('storageId')
            print(current_pill)
            if hasattr(request.user, 'manager'):
                if current_order:
                    current_order = current_order[0]
                    existed_pill_in_basket = models.Basket.objects.filter(order_id=current_order, pill_id__id=current_pill)
                    if existed_pill_in_basket:
                        existed_pill_in_basket = existed_pill_in_basket[0]
                        existed_pill_in_basket.count += 1
                        existed_pill_in_basket.save()
                    else:
                        new_pill_in_basket = models.Basket(order_id=current_order, pill_id=models.Pill.objects.get(pk=current_pill), count=1)
                        new_pill_in_basket.save()
                else:
                    new_order = models.Order(manager_id=request.user.manager, pharmacy_id=request.user.manager.pharmacy_id, is_agreed=False, date=datetime.datetime.now())
                    new_order.save()
                    new_pill_in_basket = models.Basket(order_id=new_order, pill_id=models.Pill.objects.get(pk=current_pill), count=1)
                    new_pill_in_basket.save()
            else:
                if current_order:
                    models.Basket()
                else:
                    models.Order()
        if 'search' in request.GET:
            if request.GET.get('global_check'):
                context['pills_list'] = []
                pills = django_admin_keyword_search(models.Pill,
                                                    request.GET.get('search_input'),
                                                    ['name', 'category', 'cost', 'country'])
                for pill in pills:
                    context['pills_list'].extend(models.Storage.objects.filter(
                        pill_id__id=pill.id))
            else:
                if hasattr(request.user, 'manager'):
                    context['pills_list'] = []
                    pills = django_admin_keyword_search(models.Pill,
                                                        request.GET.get('search_input'),
                                                        ['name', 'category', 'cost', 'country'])
                    for pill in pills:
                        context['pills_list'].extend(models.Storage.objects.filter(
                            pill_id__id=pill.id, pharmacy_id=request.user.manager.pharmacy_id))
                elif hasattr(request.user, 'seller'):
                    context['pills_list'] = []
                    pills = django_admin_keyword_search(models.Pill,
                                                        request.GET.get('search_input'),
                                                        ['name', 'category', 'cost', 'country'])
                    for pill in pills:
                        context['pills_list'].extend(models.Storage.objects.filter(
                            pill_id__id=pill.id, pharmacy_id=request.user.seller.pharmacy_id))
                else:
                    context['pills_list'] = []
                    pills = django_admin_keyword_search(models.Pill,
                                                        request.GET.get('search_input'),
                                                        ['name', 'category', 'cost', 'country'])
                    for pill in pills:
                        context['pills_list'].extend(models.Storage.objects.filter(
                            pill_id__id=pill.id))
        return render(request, self.template_name, self.get_context_data(request, **context))

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(request))


class Recipes(LoginRequiredMixin, View):
    template_name = 'pages/recipes.html'

    def get_context_data(self, **kwargs):
        if 'recipes_list' not in kwargs:
            kwargs['recipes_list'] = models.Recipe.objects.all()[:15]
        return kwargs

    def get(self, request, *args, **kwargs):
        context = {}
        if 'search' in request.GET:
            context['recipes_list'] = []
            context['recipes_list'] = django_admin_keyword_search(models.Recipe,
                                                                  request.GET.get('search_input'),
                                                                  ['pill_name', 'doctor'])
        return render(request, self.template_name, self.get_context_data(**context))


class Orders(LoginRequiredMixin, View):
    template_name = 'pages/orders.html'

    def get_context_data(self, **kwargs):
        kwargs['items_list'] = models.Basket.objects.filter(order_id__is_agreed=False)
        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        ctxt = {}

        if 'pill_search_name' in request.POST:
            response_form = PillSearchName(request.POST)
            if response_form.is_valid():
                pass
            else:
                ctxt['response_form'] = response_form

        return render(request, self.template_name, self.get_context_data(**ctxt))


class Signup(View):
    form_class = UserCreationForm
    initial = {'key': 'value'}
    template_name = 'registration/signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
