from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.models import Permission
from django.contrib.auth.mixins import UserPassesTestMixin


class SuperUserCheck(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'form.html'

    def form_valid(self, form):
        response = super(SignUpView, self).form_valid(form)
        login(self.request, self.object)
        return response


class CreateAdmin(SuperUserCheck, CreateView):
    form_class = UserCreationForm
    success_url = '/'
    template_name = 'form.html'

    def form_valid(self, form):
        response = super(CreateAdmin, self).form_valid(form)
        user = self.object
        perms = list(Permission.objects.filter(content_type_id__in=[7, 8, 9, 10, 11]))
        user.user_permissions.set(perms)
        return response
