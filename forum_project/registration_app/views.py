from typing import Any
from django import http
from django.shortcuts import render

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import CreateView, FormView, TemplateView
from django.urls import reverse_lazy
from .forms import CreateUserForm, LoginUserForm
from .models import UserProfile


# Create your views here.

class CreateUserView(CreateView):
    """
    View to create User objects
    """
    form_class = CreateUserForm
    template_name = "register.html"
    success_url = reverse_lazy("login") 

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
        # Do something for authenticated users.
            messages.error(request, "{}, first you have to log-out, to sign up".format(request.user.get_username()))
            return HttpResponseRedirect(self.success_url)
        else:
            form = self.form_class()
        return render(request, template_name="register.html", context={"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user_profile = UserProfile.objects.create(owner=form.save())
            user_profile.save()
            messages.success(request, "Registration succesful!")
            return HttpResponseRedirect(self.success_url)
        else:
            messages.error(request, "Form is not valid!")
            return render(request, self.template_name, {'form': form})

class LoginView(FormView):
    form_class = LoginUserForm
    template_name = "login.html"

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            messages.error(request, "{}, first you have to log-out, to sign up".format(request.user.get_username()))
            return HttpResponseRedirect(reverse_lazy('index'))
        else:
            form = self.form_class()
            context = {"form": form}
        return render(request, self.template_name, context=context)
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, "Welcome user, {} !".format(user.get_username()))
                return HttpResponseRedirect(reverse_lazy('index'))
            else:
                messages.error(request, "Invalid user!")
                return render(request, self.template_name, {'form': form})

class LogoutView(TemplateView):
    success_url = reverse_lazy('index')

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        if request.user.is_authenticated:
            logout(request)
            return HttpResponseRedirect(self.success_url)
        else:
            messages.error(request, "Invalid user!")
            return render(request, self.success_url)

class UserProfileView():
    #TODO
    pass