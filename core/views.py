import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from . import models
from .utils import django_admin_keyword_search


class Home(TemplateView):
    template_name = 'home.html'


class Pills(LoginRequiredMixin, View):
    template_name = 'pages/pills.html'

    def get_context_data(self, request, **kwargs):
        if 'pills_list' not in kwargs:
            if hasattr(request.user, 'manager'):
                kwargs['pills_list'] = models.Storage.objects.filter(pharmacy_id=request.user.manager.pharmacy_id).order_by('id')[:15]
            elif hasattr(request.user, 'seller'):
                kwargs['pills_list'] = models.Storage.objects.filter(
                    pharmacy_id=request.user.seller.manager_id.pharmacy_id).order_by('id')[:15]
            else:
                kwargs['pills_list'] = models.Storage.objects.all().order_by('id')[:15]
        return kwargs

    def get(self, request, *args, **kwargs):
        context = {}
        self.user_seller = None
        self.user_manager = None
        if hasattr(request.user, 'manager'):
            self.user_manager = request.user.manager
        if hasattr(request.user, 'seller'):
            self.user_seller = request.user.seller
        if 'storageId' in request.GET:
            try:
                current_storage = request.GET.get('storageId')
                current_pill = models.Storage.objects.get(pk=current_storage).pill_id
                if hasattr(request.user, 'manager'):
                    current_order = models.Order.objects.filter(Q(is_agreed=False) &
                                                                Q(pharmacy_id=self.user_manager.pharmacy_id) &
                                                                Q(manager_id=self.user_manager))
                    if current_order:
                        current_order = current_order[0]
                        existed_pill_in_basket = models.Basket.objects.filter(order_id=current_order,
                                                                              pill_id__id=current_pill.id)
                        if existed_pill_in_basket:
                            existed_pill_in_basket = existed_pill_in_basket[0]
                            existed_pill_in_basket.count += 1
                            edited_pill = models.Storage.objects.get(pk=current_storage)
                            edited_pill.count -= 1
                            edited_pill.save()
                            existed_pill_in_basket.save()
                        else:
                            new_pill_in_basket = models.Basket(order_id=current_order,
                                                               pill_id=models.Pill.objects.get(pk=current_pill.id),
                                                               count=1)
                            edited_pill = models.Storage.objects.get(pk=current_storage)
                            edited_pill.count -= 1
                            edited_pill.save()
                            new_pill_in_basket.save()
                    else:
                        new_order = models.Order(manager_id=request.user.manager,
                                                 pharmacy_id=request.user.manager.pharmacy_id, is_agreed=False,
                                                 date=datetime.datetime.now())
                        new_order.save()
                        new_pill_in_basket = models.Basket(order_id=new_order,
                                                           pill_id=models.Pill.objects.get(pk=current_pill.id), count=1)
                        edited_pill = models.Storage.objects.get(pk=current_storage)
                        edited_pill.count -= 1
                        edited_pill.save()
                        new_pill_in_basket.save()
                else:
                    current_order = models.Order.objects.filter(Q(is_agreed=False) &
                                                                Q(pharmacy_id=self.user_seller.manager_id.pharmacy_id) &
                                                                Q(seller_id=self.user_seller))
                    if current_order:
                        current_order = current_order[0]
                        existed_pill_in_basket = models.Basket.objects.filter(order_id=current_order,
                                                                              pill_id__id=current_pill.id)
                        if existed_pill_in_basket:
                            existed_pill_in_basket = existed_pill_in_basket[0]
                            existed_pill_in_basket.count += 1
                            edited_pill = models.Storage.objects.get(pk=current_storage)
                            edited_pill.count -= 1
                            edited_pill.save()
                            existed_pill_in_basket.save()
                        else:
                            new_pill_in_basket = models.Basket(order_id=current_order,
                                                               pill_id=models.Pill.objects.get(pk=current_pill.id),
                                                               count=1)
                            edited_pill = models.Storage.objects.get(pk=current_storage)
                            edited_pill.count -= 1
                            edited_pill.save()
                            new_pill_in_basket.save()
                    else:
                        new_order = models.Order(seller_id=request.user.seller,
                                                 pharmacy_id=request.user.seller.manager_id.pharmacy_id,
                                                 is_agreed=False,
                                                 date=datetime.datetime.now())
                        new_order.save()
                        new_pill_in_basket = models.Basket(order_id=new_order,
                                                           pill_id=models.Pill.objects.get(pk=current_pill.id), count=1)
                        edited_pill = models.Storage.objects.get(pk=current_storage)
                        edited_pill.count -= 1
                        edited_pill.save()
                        new_pill_in_basket.save()
                return HttpResponse(status=201, content="Успешно добавлено в корзину")
            except Exception as e:
                print(e)
                return HttpResponse(status=500, content="Ошибка при добавлении в корзину")

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
                            pill_id__id=pill.id, pharmacy_id=request.user.seller.manager_id.pharmacy_id))
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
            kwargs['recipes_list'] = models.Recipe.objects.filter(is_used=False)[:15]
        return kwargs

    def get(self, request, *args, **kwargs):
        context = {}

        if 'recipe_id' in request.GET:
            try:
                recipe_id = request.GET.get('recipe_id')
                current_recipe = models.Recipe.objects.get(pk=recipe_id)
                pill_id = models.Pill.objects.filter(recipe_id=recipe_id)[0]
                if hasattr(request.user, 'manager'):
                    pharmacy_id = request.user.manager.pharmacy_id
                else:
                    pharmacy_id = request.user.seller.manager_id.pharmacy_id
                if hasattr(request.user, 'manager'):
                    current_order = models.Order.objects.filter(Q(is_agreed=False) &
                                                                Q(pharmacy_id=pharmacy_id) &
                                                                Q(manager_id=request.user.manager))
                else:
                    current_order = models.Order.objects.filter(Q(is_agreed=False) &
                                                                Q(pharmacy_id=pharmacy_id) &
                                                                Q(seller_id=request.user.seller))
                if current_order:
                    current_order = current_order[0]
                    existed_pill_in_basket = models.Basket.objects.filter(order_id=current_order, pill_id=pill_id)
                    if existed_pill_in_basket:
                        existed_pill_in_basket = existed_pill_in_basket[0]
                        existed_pill_in_basket.count += current_recipe.count_by_recipe
                        edited_pill = models.Storage.objects.filter(pill_id=pill_id, pharmacy_id=pharmacy_id)[0]
                        edited_pill.count -= current_recipe.count_by_recipe
                        edited_pill.full_clean()
                        edited_pill.save()
                        existed_pill_in_basket.full_clean()
                        existed_pill_in_basket.save()
                    else:
                        new_pill_in_basket = models.Basket(order_id=current_order,
                                                           pill_id=pill_id,
                                                           count=current_recipe.count_by_recipe)
                        edited_pill = models.Storage.objects.filter(pill_id=pill_id, pharmacy_id=pharmacy_id)[0]
                        edited_pill.count -= current_recipe.count_by_recipe
                        edited_pill.full_clean()
                        edited_pill.save()
                        new_pill_in_basket.full_clean()
                        new_pill_in_basket.save()
                        current_recipe.is_used = True
                        current_recipe.save()
                else:
                    if hasattr(request.user, 'manager'):
                        new_order = models.Order(manager_id=request.user.manager,
                                                 pharmacy_id=pharmacy_id,
                                                 is_agreed=False,
                                                 date=datetime.datetime.now())
                    else:
                        new_order = models.Order(seller_id=request.user.seller,
                                                 pharmacy_id=pharmacy_id,
                                                 is_agreed=False,
                                                 date=datetime.datetime.now())
                    new_order.full_clean()
                    new_order.save()
                    try:
                        new_pill_in_basket = models.Basket(order_id=new_order,
                                                           pill_id=pill_id,
                                                           count=current_recipe.count_by_recipe)
                        edited_pill = models.Storage.objects.filter(pill_id=pill_id, pharmacy_id=pharmacy_id)[0]
                        edited_pill.count -= current_recipe.count_by_recipe
                        edited_pill.full_clean()
                        new_pill_in_basket.full_clean()
                        edited_pill.save()
                        new_pill_in_basket.save()
                        current_recipe.is_used = True
                        current_recipe.save()
                    except Exception as e:
                        print(e)
                        new_order.delete()
                return HttpResponse(status=201, content="Успешно добавлено в корзину")
            except Exception as e:
                print(e)
                return HttpResponse(status=500, content="Ошибка при добавлении в корзину")

        if 'search' in request.GET:
            context['recipes_list'] = []
            context['recipes_list'] = django_admin_keyword_search(models.Recipe,
                                                                  request.GET.get('search_input'),
                                                                  ['pill_name', 'doctor'])
        return render(request, self.template_name, self.get_context_data(**context))


class Orders(LoginRequiredMixin, View):
    template_name = 'pages/orders.html'

    def get_context_data(self, request, **kwargs):
        if hasattr(request.user, 'seller'):
            kwargs['items_list'] = models.Basket.objects.filter(Q(order_id__is_agreed=False) &
                                                                Q(order_id__pharmacy_id=self.user_seller.manager_id.pharmacy_id) &
                                                                Q(order_id__seller_id=self.user_seller)).order_by(
                'pill_id')
        if hasattr(request.user, 'manager'):
            kwargs['items_list'] = models.Basket.objects.filter(Q(order_id__is_agreed=False) &
                                                                Q(order_id__pharmacy_id=self.user_manager.pharmacy_id) &
                                                                Q(order_id__manager_id=self.user_manager)).order_by(
                'pill_id')

        kwargs['final_cost'] = 0
        for item in kwargs['items_list']:
            kwargs['final_cost'] += item.count * item.pill_id.cost
        return kwargs

    def get(self, request, *args, **kwargs):
        self.user_seller = None
        self.user_manager = None
        if hasattr(request.user, 'manager'):
            self.user_manager = request.user.manager
        if hasattr(request.user, 'seller'):
            self.user_seller = request.user.seller
            self.user_manager = request.user.seller.manager_id

        if 'add_count' in request.GET:
            context = {}
            current_basket = models.Basket.objects.get(pk=request.GET.get('add_count'))
            current_storage = models.Storage.objects.filter(pill_id=current_basket.pill_id,
                                                            pharmacy_id=current_basket.order_id.pharmacy_id)[0]
            if current_storage.count > 0:
                current_basket.count += 1
                current_storage.count -= 1
                current_storage.save()
                current_basket.save()
            else:
                return HttpResponse(status=500, content="Ошибка при добавлении в корзину")

            return render(request, self.template_name, self.get_context_data(request, **context))

        if 'delete_count' in request.GET:
            context = {}
            current_basket = models.Basket.objects.get(pk=request.GET.get('delete_count'))
            current_storage = models.Storage.objects.filter(pill_id=current_basket.pill_id,
                                                            pharmacy_id=current_basket.order_id.pharmacy_id)[0]
            current_basket.count -= 1
            current_storage.count += 1
            current_storage.save()
            current_basket.save()
            if current_basket.count == 0:
                current_basket.delete()
            return render(request, self.template_name, self.get_context_data(request, **context))

        return render(request, self.template_name, self.get_context_data(request))

    def post(self, request, *args, **kwargs):
        self.user_seller = None
        self.user_manager = None
        if hasattr(request.user, 'manager'):
            self.user_manager = request.user.manager
        if hasattr(request.user, 'seller'):
            self.user_seller = request.user.seller
            self.user_manager = request.user.seller.manager_id

        if hasattr(request.user, 'manager'):
            pharmacy_id = request.user.manager.pharmacy_id
        else:
            pharmacy_id = request.user.seller.manager_id.pharmacy_id

        if 'cancel_order' in request.POST:
            if hasattr(request.user, 'manager'):
                current_order = models.Order.objects.filter(Q(is_agreed=False) &
                                                            Q(pharmacy_id=pharmacy_id) &
                                                            Q(manager_id=request.user.manager))
            else:
                current_order = models.Order.objects.filter(Q(is_agreed=False) &
                                                            Q(pharmacy_id=pharmacy_id) &
                                                            Q(seller_id=request.user.seller))
            if current_order:
                current_order = current_order[0]
                baskets = models.Basket.objects.filter(order_id=current_order)
                for basket in baskets:
                    if basket:
                        print(basket.count)
                        current_pill = models.Storage.objects.filter(pill_id=basket.pill_id, pharmacy_id=pharmacy_id)[0]
                        print(current_pill.count)
                        current_pill.count += basket.count
                        current_pill.save()

                current_order.delete()


        if 'create_order' in request.POST:
            if hasattr(request.user, 'manager'):
                current_order = models.Order.objects.filter(Q(is_agreed=False) &
                                                            Q(pharmacy_id=pharmacy_id) &
                                                            Q(manager_id=request.user.manager))
            else:
                current_order = models.Order.objects.filter(Q(is_agreed=False) &
                                                            Q(pharmacy_id=pharmacy_id) &
                                                            Q(seller_id=request.user.seller))
            if current_order:
                current_order = current_order[0]
                current_order.is_agreed = True
                current_order.save()
        return render(request, self.template_name, self.get_context_data(request))


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
