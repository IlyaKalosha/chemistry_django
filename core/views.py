from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView
from .forms import (
    PillSearchName, PillSearchCategory, PillSearchCost, PillSearchDate, AddPill, UpdatePill, DeletePill,
    RecipeSearchDate, RecipeSearchDoctor, DeleteRecipe, AddRecipe, UpdateRecipe)
from . import models


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
        if 'form_pills_search_name' not in kwargs:
            kwargs['form_pills_search_name'] = PillSearchName()
        if 'form_pill_search_category' not in kwargs:
            kwargs['form_pill_search_category'] = PillSearchCategory()
        if 'form_pill_search_cost' not in kwargs:
            kwargs['form_pill_search_cost'] = PillSearchCost()
        if 'form_pill_search_date' not in kwargs:
            kwargs['form_pill_search_date'] = PillSearchDate()
        if 'form_pill_add' not in kwargs:
            kwargs['form_pill_add'] = AddPill()
        if 'form_pill_update' not in kwargs:
            kwargs['form_pill_update'] = UpdatePill()
        if 'form_pill_delete' not in kwargs:
            kwargs['form_pill_delete'] = DeletePill()
        return kwargs

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data(request))

    def post(self, request, *args, **kwargs):
        context = {}

        if 'pill_search_name' in request.POST:
            response_form = PillSearchName(request.POST)
            if response_form.is_valid():
                if response_form.cleaned_data['is_search_global']:
                    context['pills_list'] = models.Storage.objects.filter(
                        pill_id__name=response_form.cleaned_data['pill_name'])
                else:
                    if hasattr(request.user, 'manager'):
                        context['pills_list'] = models.Storage.objects.filter(
                            pill_id__name=response_form.cleaned_data['pill_name'],
                            pharmacy_id=request.user.manager.pharmacy_id
                        )
                    elif hasattr(request.user, 'seller'):
                        context['pills_list'] = models.Storage.objects.filter(
                            pill_id__name=response_form.cleaned_data['pill_name'],
                            pharmacy_id=request.user.seller.manager_id.pharmacy_id
                        )
                    else:
                        context['pills_list'] = models.Storage.objects.filter(
                            pill_id__name=response_form.cleaned_data['pill_name'])
            else:
                context['form_pills_search_name'] = response_form

        if 'pill_search_category' in request.POST:
            response_form = PillSearchCategory(request.POST)
            if response_form.is_valid():
                if response_form.cleaned_data['is_search_global']:
                    context['pills_list'] = models.Storage.objects.filter(
                        pill_id__category=response_form.cleaned_data['category'])
                else:
                    if hasattr(request.user, 'manager'):
                        context['pills_list'] = models.Storage.objects.filter(
                            pill_id__category=response_form.cleaned_data['category'],
                            pharmacy_id=request.user.manager.pharmacy_id
                        )
                    elif hasattr(request.user, 'seller'):
                        context['pills_list'] = models.Storage.objects.filter(
                            pill_id__category=response_form.cleaned_data['category'],
                            pharmacy_id=request.user.seller.manager_id.pharmacy_id
                        )
                    else:
                        context['pills_list'] = models.Storage.objects.filter(
                            pill_id__category=response_form.cleaned_data['category'])
            else:
                context['form_pill_search_category'] = response_form

        if 'pill_search_cost' in request.POST:
            response_form = PillSearchCost(request.POST)
            if response_form.is_valid():
                if hasattr(request.user, 'manager'):
                    context['pills_list'] = models.Storage.objects.filter(
                        pill_id__category=response_form.cleaned_data['category'],
                        pharmacy_id=request.user.manager.pharmacy_id
                    )
                elif hasattr(request.user, 'seller'):
                    context['pills_list'] = models.Storage.objects.filter(
                        pill_id__category=response_form.cleaned_data['category'],
                        pharmacy_id=request.user.seller.manager_id.pharmacy_id
                    )
                else:
                    context['pills_list'] = models.Storage.objects.filter(
                        pill_id__category=response_form.cleaned_data['category'])
            else:
                context['form_pill_search_category'] = response_form

        return render(request, self.template_name, self.get_context_data(request, **context))


class Recipes(LoginRequiredMixin, View):
    template_name = 'pages/recipes.html'

    def get_context_data(self, **kwargs):
        kwargs['recipes_list'] = models.Recipe.objects.all()
        if 'form_recipe_search_doctor' not in kwargs:
            kwargs['form_recipe_search_doctor'] = RecipeSearchDoctor()
        if 'form_recipe_search_date' not in kwargs:
            kwargs['form_recipe_search_date'] = RecipeSearchDate()
        if 'form_recipe_add' not in kwargs:
            kwargs['form_recipe_add'] = AddRecipe()
        if 'form_recipe_update' not in kwargs:
            kwargs['form_recipe_update'] = UpdateRecipe()
        if 'form_recipe_delete' not in kwargs:
            kwargs['form_recipe_delete'] = DeleteRecipe()
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


class Sellers(LoginRequiredMixin, View):
    template_name = 'pages/sellers.html'

    def get_context_data(self, **kwargs):
        kwargs['pills_list'] = Storage.objects.all()
        if 'form_pills_search_name' not in kwargs:
            kwargs['form_pills_search_name'] = PillSearchName()
        if 'form_pill_search_category' not in kwargs:
            kwargs['form_pill_search_category'] = PillSearchCategory()
        if 'form_pill_search_cost' not in kwargs:
            kwargs['form_pill_search_cost'] = PillSearchCost()
        if 'form_pill_search_date' not in kwargs:
            kwargs['form_pill_search_date'] = PillSearchDate()
        if 'form_pill_add' not in kwargs:
            kwargs['form_pill_add'] = AddPill()
        if 'form_pill_update' not in kwargs:
            kwargs['form_pill_update'] = UpdatePill()
        if 'form_pill_delete' not in kwargs:
            kwargs['form_pill_delete'] = DeletePill()
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


class Storage(LoginRequiredMixin, View):
    template_name = 'pages/storage.html'

    def get_context_data(self, **kwargs):
        kwargs['pills_list'] = Storage.objects.all()
        if 'form_pills_search_name' not in kwargs:
            kwargs['form_pills_search_name'] = PillSearchName()
        if 'form_pill_search_category' not in kwargs:
            kwargs['form_pill_search_category'] = PillSearchCategory()
        if 'form_pill_search_cost' not in kwargs:
            kwargs['form_pill_search_cost'] = PillSearchCost()
        if 'form_pill_search_date' not in kwargs:
            kwargs['form_pill_search_date'] = PillSearchDate()
        if 'form_pill_add' not in kwargs:
            kwargs['form_pill_add'] = AddPill()
        if 'form_pill_update' not in kwargs:
            kwargs['form_pill_update'] = UpdatePill()
        if 'form_pill_delete' not in kwargs:
            kwargs['form_pill_delete'] = DeletePill()
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


class Orders(LoginRequiredMixin, View):
    template_name = 'pages/orders.html'

    def get_context_data(self, **kwargs):
        kwargs['pills_list'] = models.Order.objects.all()
        if 'form_pills_search_name' not in kwargs:
            kwargs['form_pills_search_name'] = PillSearchName()
        if 'form_pill_search_category' not in kwargs:
            kwargs['form_pill_search_category'] = PillSearchCategory()
        if 'form_pill_search_cost' not in kwargs:
            kwargs['form_pill_search_cost'] = PillSearchCost()
        if 'form_pill_search_date' not in kwargs:
            kwargs['form_pill_search_date'] = PillSearchDate()
        if 'form_pill_add' not in kwargs:
            kwargs['form_pill_add'] = AddPill()
        if 'form_pill_update' not in kwargs:
            kwargs['form_pill_update'] = UpdatePill()
        if 'form_pill_delete' not in kwargs:
            kwargs['form_pill_delete'] = DeletePill()
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
