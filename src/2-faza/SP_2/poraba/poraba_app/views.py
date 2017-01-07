from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
import random
from django.urls import reverse
# form
# Create your views here.
from django.http import HttpResponse

app_name = 'poraba_app'


def filterPoraba(a):
    return a.povprecna_poraba1()


def index(request):
    # cene goriv + random user
    context = {}
    cifra = random.randrange(2, 5)
    nakljucniU = User.objects.get(pk=cifra)
    context['uporabnik'] = nakljucniU
    avto = Avtomobil.objects.filter(user_id=nakljucniU)
    context['avto'] = avto[0]
    poraba = Poraba.objects.filter(user_id=nakljucniU, avto_id=avto[0])
    context['poraba'] = poraba[0].poraba
    return render(request, 'poraba_app/index.html', context)


def najs_10(request):
    # preberi 5 avtomobilov z najvecjo porabo
    context = {}
    avti = Avtomobil.objects
    list = avti.all()
    najs10 = sorted(list, key=lambda a: filterPoraba(a), reverse=True)[:10]
    context['avti'] = najs10
    return render(request, 'poraba_app/najs_10.html', context)


def najb_10(request):
    # preberi 5 avtomobilov z najmanjso porabo
    context = {}
    avti = Avtomobil.objects
    list = avti.all()
    najs10 = sorted(list, key=lambda a: filterPoraba(a))[:10]
    context['avti'] = najs10
    return render(request, 'poraba_app/najb_10.html', context)


def o_nas(request):
    # opis
    return render(request, 'poraba_app/o_nas.html')


def prijava(request):
    context = {}
    if request.method == 'POST':
        form = prijavaForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                context['sporocilo'] = "Prijavljeni."
            else:
                context['sporocilo'] = "Nekaj je šlo narobe. Prosim poskusite ponovno."
        else:
            context['sporocilo'] = "Neveljavni podatki."
    else:
        form = prijavaForm()

    context['prijavaForm'] = form
    return render(request, 'poraba_app/prijava.html', context)


def registracija(request):
    context = {}

    if request.method == 'POST':
        form = registracijaForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            geslo1 = form.cleaned_data['password1']
            geslo2 = form.cleaned_data['password2']
            if geslo1 == geslo2:
                uporabnik = User.objects.create_user(username=username, password=geslo2)
                uporabnik.save()
                context['sporocilo'] = "Registracija uspela."
            else:
                context['sporocilo'] = "Ponovno vnesite gesla."
        else:
            context['sporocilo'] = "Napaka."
    else:
        form = registracijaForm()
        context['sporocilo'] = ""
    context['registracijaForm'] = form
    return render(request, 'poraba_app/registracija.html', context)


def logout1(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def moja(request):
    context = {}
    if request.user.is_authenticated:
        user = request.user
        avti = Avtomobil.objects.filter(user_id=user)
        list = avti.all()
        najs10 = sorted(list, key=lambda a: filterPoraba(a))[:10]
        context['avti'] = najs10

        if request.method == 'POST':
            form = dodajAvtoForm(request.POST)
            if form.is_valid():
                avto = Avtomobil(ime_vozila=form.cleaned_data['ime'], tip_goriva=form.cleaned_data['gorivo_tip'],
                                 user_id=user)

                if avto is not None:
                    avto.save()
                    # print(avto.id)
                    p = Poraba(poraba=form.cleaned_data['poraba_vozila'], avto_id=avto, user_id=user)
                    p.save()
            else:
                print("imhere")
        else:
            form = dodajAvtoForm

        context['dodajAvtoForm'] = form

    return render(request, 'poraba_app/moja.html', context)


def racunalo(request):
    return render(request, 'poraba_app/racunalo.html')


def iskanje(request):
    # uzamm iz forma vn string in poiscem in vracam na novi strani avte
    context = {}

    if request.method == 'GET':
        form = iskanjeForm(request.GET)
        if form.is_valid():
            niz = form.cleaned_data['iskalni_niz']

            avti = Avtomobil.objects.filter(ime_vozila__contains=niz)
            list = avti.all()
            najs10 = sorted(list, key=lambda a: filterPoraba(a))[:10]

            if avti:
                context['avti'] = najs10
            else:
                context['Sporocilo'] = "Ni najdenih vozil"
        else:
            context['sporocilo'] = "Za prikaz avtomobilov vnsei znamko ali del imena vozila."
    else:
        form = iskanjeForm()
        context['sporocilo'] = "jaaaaaaaaaa"
    context['iskanjeForm'] = form
    return render(request, 'poraba_app/iskanje.html', context)


def poraba(request, car_id):
    context = {}
    avto = Avtomobil.objects.get(id=car_id)
    context['avto'] = avto
    user = request.user
    # print(user)
    # print(avto.id)
    porabe = Poraba.objects.filter(avto_id=avto.id, user_id=user).order_by('-datum')
    context['porabe'] = porabe

    if request.method == 'POST':
        form = porabaForm(request.POST)
        if form.is_valid():
            pOraba = form.cleaned_data['p']
            # avto_id=car_id?
            poRaba = Poraba(poraba=pOraba, avto_id=avto, user_id=user)
            poRaba.save()
    else:
        form = porabaForm
    context['porabaForm'] = form

    return render(request, 'poraba_app/poraba.html', context)
