from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import ListView
from .models import BenchtopDrugLocations


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class BenchtopDrugLocationView(ListView):
    model = BenchtopDrugLocations
    template_name = 'drug_db/basic_all_cmpd_loc_view.html'