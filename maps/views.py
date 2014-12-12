from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render

from maps.models import *


def index(request):
    trips_list = Trip.objects.order_by('trip_name')[:5]
    template = loader.get_template('maps/index.html')
    context = RequestContext(request, {
        'trips_list': trips_list,
    })
    return HttpResponse(template.render(context))


def detail(request, trip_id):
    trip = get_object_or_404(Trip, pk=trip_id)
    return render(request, 'maps/trip.html', {'trip': trip})