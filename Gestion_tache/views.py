from django.shortcuts import render
from .forms import TacheForm
# Create your views here.

def tache_list(request):
    return render(request,"Gestion_tache/tache_list.html")

def tache_form(request):
    form = TacheForm()
    return render(request,"Gestion_tache/tache_form.html",{'form':form})

def tache_delete(request):
    return