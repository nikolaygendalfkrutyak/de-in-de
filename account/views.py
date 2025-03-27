from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView

from account.forms import LoginForm, RegistrationForm,  UserUpdateForm
from account.models import CustomUser


# Create your views here.

class UserLoginView(LoginView):
    template_name = 'sign_in.html'
    form_class = LoginForm

    def get_success_url(self):
        
        return self.request.GET.get("next","/")

class UserRegistrationView(CreateView):
    template_name ='sign_up.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('sign_in')
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = 'account_settings.html'
    success_url = reverse_lazy('home')  # Redirect after update

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Re-login after password change
        return super().form_valid(form)

def logout_view(request):
    logout(request)
    return redirect('home')





