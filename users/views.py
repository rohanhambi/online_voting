from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import ListView,TemplateView
from django.shortcuts import render, redirect
from .models import *
from .forms import PartiesForm
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


def parties_new(request):
    form = PartiesForm()
    return render(request, 'parties.html', {'form': form})
'''
def parties_hi(request):
    parties_logo = request.GET["parties_logo"]
    parties_description = request.GET["parties_description"]
    parties_info = Parties(parties_logo=parties_logo,
                               parties_description=parties_description
                               )
    parties_info.save()
    all_parties = Parties.objects.all()
    return render(request, 'parties.html', {'parties': all_partie

def parties(request):
    return redirect(request=request,
                  template_name="parties.html",
                  context={"parties": Parties.objects.all})
'''

def votenow(request):
    return redirect(request=request,
                  template_name="votenow.html",
                  context={"parties":  Parties.objects.all})