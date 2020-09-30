from django.urls import reverse_lazy
from django.views import generic
from django.views import View
from django.shortcuts import render, redirect
from .models import User
from .forms import SingUpForm
from .forms import ProfileForm


class SignUpView(generic.CreateView):
    form_class = SingUpForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        user_data = User.objects.get(user_id=request.user.user_id)

        return render(request, "accounts/profile.html", {"user_data": user_data})


class ProfileEditView(View):
    def get(self, request):
        user_data = User.objects.get(user_id=request.user.user_id)
        form = ProfileForm(
            request.POST or None,
            initial={
                "username": user_data.username,
                "email": user_data.email,
            }
        )

        return render(request, "accounts/prof_edit.html", {"form": form})

    def post(self, request):
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            user_data = User.objects.get(user_id=request.user.user_id)
            user_data.username = form.cleaned_data["username"]
            user_data.email = form.cleaned_data["email"]
            user_data.save()
            return redirect("http://127.0.0.1:8000/accounts/profile")

        return render(request, "accounts/profile.html", {"form": form})
