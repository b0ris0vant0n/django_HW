import csv
from csv import DictReader

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    with open('data-398-2018-08-30.csv', encoding='UTF-8') as csvfile:
        reader = csv.DictReader(csvfile)
        stations_list = []
        for row in reader:
            station = {
                'Name': row['Name'],
                'Street': row['Street'],
                'District': row['District']
            }
            stations_list.append(station)
    page_number = request.GET.get('page', 1)
    paginator = Paginator(stations_list, 10)
    page = paginator.get_page(page_number)
    CONTENT = page.object_list


    context = {
        'bus_stations': CONTENT,
        'page': page,
    }
    return render(request, 'stations/index.html', context)

