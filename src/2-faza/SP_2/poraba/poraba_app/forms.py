from django import forms
from django.contrib.auth.models import User
from .models import *


class prijavaForm(forms.Form):
    username = forms.CharField(label="")
    password = forms.CharField(label="", widget=forms.PasswordInput)


class registracijaForm(forms.Form):
    username = forms.CharField(label="")
    password1 = forms.CharField(label="", widget=forms.PasswordInput)
    password2 = forms.CharField(label="", widget=forms.PasswordInput)


class iskanjeForm(forms.Form):
    iskalni_niz = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Iskanje po znamkah'}))


class dodajAvtoForm(forms.Form):
    ime = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'VW Golf 1.4'}))
    poraba_vozila = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': '6.8'}))
    gorivo_tip = forms.ChoiceField(choices=(
            ("Bencin 100", "Bencin 100"),
            ("Bencin 95", "Bencin 95"),
            ("Dizel", "Dizel"),
        ))


class porabaForm(forms.Form):
    p = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': '6.8'}))
