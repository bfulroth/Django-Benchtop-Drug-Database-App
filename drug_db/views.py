
# Create your views here.
from django.http import HttpResponse

# Import models to be rendered as views.
from .models import BenchtopDrugLocations

from django.views.generic import ListView
from django_tables2 import SingleTableView
from .tables import DrugLocationTable


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class BenchtopDrugLocationView(ListView):
    model = BenchtopDrugLocations
    template_name = 'drug_db/basic_all_cmpd_loc_view.html'


class BenchtopDrugLocationView2(SingleTableView):
    # Turn off Pagination
    SingleTableView.table_pagination = False

    model = BenchtopDrugLocations
    table_class = DrugLocationTable
    template_name = 'drug_db/basic2_all_cmpd_loc_view.html'