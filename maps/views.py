from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render

from maps.models import *


def index(request):
    template = loader.get_template('maps/index.html')
    context = RequestContext(request, {
    })
    return HttpResponse(template.render(context))


def nokhethas(request):
    nokhetha_list = Nokhetha.objects.order_by('nokhetha_name')[:5]
    template = loader.get_template('maps/nokhethas.html')
    context = RequestContext(request, {
        'nokhetha_list': nokhetha_list,
    })
    return HttpResponse(template.render(context))


def nokhetha_detail(request, nokh_id):
    template = loader.get_template('maps/nokhetha.html')
    nokh = get_object_or_404(Nokhetha, pk=nokh_id)
    trips = Trip.objects.filter(nokhetha=nokh)
    context = RequestContext(request, {
        'nokhetha': nokh,
        'nokhetha_trips': trips
    })

    return HttpResponse(template.render(context))


def detail(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    return render(request, 'maps/trip.html', {'trip': trip})