from django.shortcuts import render
from personal.models import Auth, Medicinereco
import random


def index(request):
    a = Medicinereco.objects.all()
    if 'name' in request.session:
        return render(request, 'personal/home.html', {'a': a, 'username': request.session['name'], 'done': 'yes'})
    else:
        return render(request, 'personal/home.html', {'a': a, 'done': 'no'})


def authentication(request):
    username = request.GET['fname1']
    password = request.GET['fname3']
    a = Medicinereco.objects.all()
    auth = Auth.objects.all()
    ishere = 0
    for rr in auth:
        if rr.user == username:
            ishere = 1
            error = True
            return render(request, 'personal/home.html', {'a': a, 'done': 'no'})

    if ishere == 0:
        a = Auth(user=username, password=password)
        a.save()
        b = Medicinereco.objects.all()
        request.session['name'] = username
        return render(request, 'personal/home.html', {'a': b, 'username': request.session['name'], 'done': 'yes'})


def login(request):
    username1 = request.GET['fname5']
    password1 = request.GET['fname6']
    b = Medicinereco.objects.all()
    log = Auth.objects.all()
    isthere = 0
    for rs in log:
        if rs.user == username1 and rs.password == password1:
            isthere = 1

    if isthere == 1:
        request.session['name'] = username1
        return render(request, 'personal/home.html', {'a': b, 'username': username1})
    else:
        return render(request, 'personal/home.html', {'a': b})


def result(request):
    sym = request.GET['sym']
    mess = Medicinereco.objects.filter(symptoms__contains=sym)
    n = random.randrange(50, 80, 1)
    if 'name' in request.session:
        if 'sym' in request.GET and request.GET['sym']:
            return render(request, 'personal/result.html', {'medicine': mess, 'query': sym, 'random': n, 'username': request.session['name']})
        else:
            error = True
            return render(request, 'personal/error.html', {'error': error})
    else:
        return render(request, 'personal/result.html', {'medicine': mess, 'query': sym, 'random': n})


def thanks(request):
    if 'name' in request.session:
        return render(request, 'personal/thanks.html', {'username': request.session['name']})
    else:
        return render(request, 'personal/thanks.html', {'done': 'no'})


def privacy(request):
    if 'name' in request.session:
        return render(request, 'personal/privacy.html', {'username': request.session['name']})
    else:
        return render(request, 'personal/privacy.html', {'done': 'no'})

def contactus(request):
    if 'name' in request.session:
        return render(request, 'personal/contactus.html', {'username': request.session['name']})
    else:
        return render(request, 'personal/contactus.html', {'done': 'no'})


def suggestions(request):
    return render(request, 'personal/suggestions.html')


def disclaimer(request):
    if 'name' in request.session:
        return render(request, 'personal/disclaimer.html', {'username': request.session['name']})
    else:
        return render(request, 'personal/disclaimer.html', {'done': 'no'})


def logout(request):
    a = Medicinereco.objects.all()
    del request.session['name']
    return render(request, 'personal/home.html', {'a': a, 'done': 'no'})

def pharmacy(request):
    if 'name' in request.session:
        return render(request, 'personal/pharmacy.html', {'username': request.session['name'],  'done': 'yes'})
    else:
        return render(request, 'personal/pharmacy.html',  {'done': 'no'})