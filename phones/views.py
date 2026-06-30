from asyncio import timeout

from .models import Manufacturer
from django.shortcuts import render, redirect
from .forms import SmartphoneForm
from datetime import date
import requests


def manufacturers_index(request):
    manufacturers = Manufacturer.objects.all()
    context = {'manufacturers': manufacturers}
    return render(request, 'phones/manufacturers.html', context)


def smartphone_create(request):
    if request.method == 'POST':
        form = SmartphoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manufacturers')
    else:
        form = SmartphoneForm()
    context = {'form': form}
    return render(request, 'phones/smartphone_create.html', context)

def importar_marca(request):
    if request.method == 'POST':
        cantidad = request.POST.get('cantidad')

        url = 'https://fakerapi.it/api/v1/companies'
        params = {"_quantity": cantidad}
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        for item in data.get('data', []):
            Manufacturer.objects.create(
                name = item.get('name', 'sin nombre'),
                country = item.get('country', 'sin pais'),
                date_founded = date.today().strftime("%Y-%m-%d"),
                webpage = item.get('contact.website', 'sin webpage'),
            )
    return render(request, 'phones/importador.html')
