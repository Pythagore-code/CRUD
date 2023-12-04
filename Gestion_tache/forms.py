from django import forms
from .models import Tache_CRUD

class TacheForm(forms.ModelForm):

    class Meta:
        model = Tache_CRUD
        fields = ('name','maindate','enddate')
        labels = {
            'name':'Tache',
            'maindate': 'Date de debut',
            'enddate': 'Date de fin'
        }