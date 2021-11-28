from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import TemplateView
from .forms import PillSearchName, PillSearchCategory, PillSearchCost, PillSearchDate, AddPill, UpdatePill, DeletePill
from .models import Storage


class Home(TemplateView):
    template_name = 'home.html'


class Pills(LoginRequiredMixin, View):
    template_name = 'pages/pills.html'

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




