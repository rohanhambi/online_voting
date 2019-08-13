from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView,TemplateView
from django.shortcuts import render, redirect
from .models import *
#from .forms import CustomUserCreationForm


class SignUp(generic.CreateView):
    #form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')


def index(request):
    if request.user.is_voters:
        return render(request, 'home')
    return render(request, 'home.html')


def homepage(request):
    return redirect(request=request,
                  template_name="homepage.html",
                  context={"voter": Voters.objects.all})


def parties(request):
    return redirect(request=request,
                  template_name="parties.html",
                  context={"parties": Parties.objects.all})


class PartiesView(ListView):
    template_name = 'parties.html'
    def get_queryset(self):
        return Parties.objects_all()


def votenow(request):
    return redirect(request=request,
                  template_name="votenow.html",
                  context={"parties":  Parties.objects.all})